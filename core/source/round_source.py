from core.db.db_func import get_db
import datetime


def get_open_round_id():
    round_ID, round_name, race_IDs = get_open_round()

    return round_ID


def get_round_id():
    db = get_db()
    cursor = db.cursor()

    current_time = datetime.datetime.now()
    args = (current_time, current_time)
    query = """SELECT round.round_id 
            FROM round JOIN race ON round.round_id = race.round_id                                           
            WHERE round.start_date <= '{}' 
            AND race.race_date >= '{}'""".format(current_time, current_time)

    try:
        cursor.execute(query, args)  # inserts the current date and time in to the above SQL query
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()


def find_open_round_id():
    print("find_open_round_id")
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    # THIS NEEEDS CHECKING BY AN SQL WIZARD

    query = """SELECT round.round_id
            FROM round JOIN race ON round.round_id = race.round_id 
            WHERE race.race_date = (SELECT MIN (race_date) FROM race) AND round.start_date <= '{}' 
            AND race.race_date >= '{}' ORDER BY race.race_date ASC""".format(current_time, current_time)

    try:
        cursor.execute(query)
        db.commit()
    except db.Error:
        return False

    return cursor.fetchone()

def find_inflight_round_id():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    # THIS NEEEDS CHECKING BY AN SQL WIZARD

    query = """SELECT round.round_id
            FROM round JOIN race ON round.round_id = race.round_id 
            WHERE race.race_date = (SELECT MIN (race_date) FROM race) AND round.closed = FALSE
            AND race.race_date <= '{}' ORDER BY race.race_date ASC""".format(current_time, current_time)

    try:
        cursor.execute(query)
        db.commit()
    except db.Error:
        return False

    return cursor.fetchone()


def get_open_round():  # Returns the round_id, round_name of the current open round, as well as a list of the race_ids of the races
    # in that round
    db, cursor = database_connect()

    current_time = datetime.datetime.now()

    args = (current_time, current_time)

    sql = """SELECT round.round_id, round.round_name, race.race_id 
            FROM round JOIN race ON round.round_id = race.round_id 
            WHERE round.start_date <= %s 
            AND race.race_date >= %s"""

    cursor.execute(sql, args)  # inserts the current date and time iin to the above SQL query

    raceIDs = []
    round_ID = 0
    round_name = ""

    for record in cursor:  # Adds the each race ID to a list of raceIDs, and updates round Idd and round_name to that of the relevant round
        raceIDs.append(record[2])
        round_ID = record[0]
        round_name = record[1]

    return round_ID, round_name, raceIDs


def get_round_snails(
        race_IDs):  # returns a list of objects, each of which contains a race id and a race_data object, each of
    # each of which specifies a snail id, snail name and trainer name of that snail

    db, cursor = database_connect()

    sql = """SELECT racecard.race_id, snails.snail_id, snails.name AS snailName, trainers.name AS trainerName 
            FROM racecard JOIN snails ON racecard.snail_id = snails.snail_id 
            JOIN trainers ON snails.trainer_id = trainers.trainer_id 
            WHERE racecard.race_id = ANY(ARRAY{});""".format(race_IDs)

    cursor.execute(sql)

    temp_races_dict = {}
    query_data = []

    for row in cursor:
        raceid = row[0]
        snailid = row[1]
        snailname = row[2]
        trainername = row[3]

        temp_snails_obj = {"snail_id": snailid, "snail_name": snailname, "trainer_name": trainername}

        if raceid in temp_races_dict:
            temp_races_dict[raceid].append(temp_snails_obj)
        else:
            temp_races_dict[raceid] = []
            temp_races_dict[raceid].append(temp_snails_obj)

    for race in temp_races_dict:
        race_obj = {"race_id": race, "race_data": temp_races_dict[race]}
        query_data.append(race_obj)

    return query_data


# Returns an object specifying a the round id and name of the current open round, as well as
# a list in the format returned by get_round_snails
def get_open_round_details():
    round_ID, round_name, race_IDs = get_open_round()
    races_snails_info = get_round_snails(race_IDs)
    round_details = {"round_id": round_ID, "round_name": round_name, "races": races_snails_info}

    return round_details


# Inserts the user's predictions into the racepredictions table
def store_predictions(user_id, race_predictions):
    db, cursor = database_connect()

    snail_race_list = []
    for race_id in race_predictions:
        snail_race_tuple = (race_id, user_id, race_predictions[race_id], datetime.datetime.now())
        snail_race_list.append(snail_race_tuple)

    sql = "INSERT INTO racepredictions (race_id, user_id, snail_id, created) VALUES (%s, %s, %s, %s);"

    try:
        cursor.executemany(sql, snail_race_list)
        db.commit()
    except db.Error as err:
        print("Error writing to DB: {}".format(err))
        return False

    return True


def database_connect():
    db = get_db()
    cursor = db.cursor()
    return db, cursor


def get_future_round_details():
    db = get_db()
    cursor = db.cursor()

    current_time = datetime.datetime.now()
    args = str(current_time)
    sql = "SELECT start_date FROM round WHERE start_date > %s"

    cursor.execute(sql, (args,))

    try:
        race_date = cursor.fetchone()
        race_date = race_date[0]

        date_diff = race_date - current_time

        days = date_diff.days
        hours = int(round(date_diff.seconds / 3600, 0))
        minutes = int(round((date_diff.seconds / 60) % 60, 0))
        date_diff_intervals = {"status": 1, "days": days, "hours": hours, "minutes": minutes}

        return date_diff_intervals

    except:
        failure = {"status": 0}
        return failure


# returns the snail name of the winner for all finished races in a round
def get_snail_name_results():
    db = get_db()
    cursor = db.cursor()

    query = """SELECT 
    snailRaceResults.race_id, 
    snailRaceResults.position, 
    snails.name, trainers.name 
FROM 
    (SELECT snailRaces.race_id, 
        snailRaces.snail_id, 
        raceresult.position 

    FROM 
        (SELECT racecard.race_id, 
            racecard.snail_id, 
            race.round_id, 
            race.race_date 
        FROM racecard 
        JOIN race ON racecard.race_id = race.race_id 

        WHERE race.round_id IN 
            (SELECT round_id 
            FROM 
                (SELECT round.round_id, 
                    MAX(round.start_date) AS start_date 
                FROM round 
                WHERE round.closed = 'f'
                GROUP BY round.round_id) AS maxDateQuery)) 
            AS snailRaces 
        JOIN raceresult ON snailRaces.race_id = raceresult.race_id 
        AND snailRaces.snail_id = raceresult.snail_id) 
    AS snailRaceResults 
    JOIN snails ON snailRaceResults.snail_id = snails.snail_id 
    JOIN trainers ON snails.trainer_id = trainers.trainer_id
    WHERE snailRaceResults.position = 1;
"""

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return (cursor.fetchall())
