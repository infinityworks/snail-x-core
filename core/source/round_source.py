from core.db.db_func import get_db
import datetime


# returns round ID and name of currently-open round, as well as a list of race IDs for that round
def get_open_round():
    db, cursor = database_connect()

    current_time = datetime.datetime.now()

    args = (current_time, current_time)

    sql = """SELECT * 
                FROM round 
                WHERE round.round_id IN 
                        (SELECT miniview.round_id 
                        FROM 
                                (SELECT round_id, 
                                        closed, 
                                        start_date, 
                                        MIN(race_date) 
                                FROM fulldataview 
                                GROUP BY round_id, closed, start_date) AS miniview 
                        WHERE closed = 'f' 
                        AND miniview.start_date < %s 
                        AND miniview.min > %s)"""
    cursor.execute(sql, args)  # inserts the current date and time in to the above SQL query

    raceIDs = []
    round_ID = 0
    round_name = ""

    # Adds the each race ID to a list of raceIDs, and updates round ID and round_name to that of the relevant round
    for record in cursor:
        raceIDs.append(record[2])
        round_ID = record[0]
        round_name = record[1]

    return round_ID, round_name, raceIDs


# Returns the round_id, round_name of the current open round, as well as a list of the race_ids of the races
def get_open_round_id():
    round_ID, round_name, race_IDs = get_open_round()

    return round_ID


def get_inflight_round_id():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()
    args = (current_time, )

    query = "SELECT DISTINCT round_id FROM fulldataview WHERE start_date < %s AND closed = 'f'"

    try:
        cursor.execute(query, args)
        db.commit()
    except db.Error:
        return False

    round_ID = cursor.fetchone()[0]

    return round_ID


# returns a list of objects, each of which contains a race id and a race_data object
# each of which specifies a snail id, snail name and trainer name of that snail
def get_round_snails(race_IDs):

    db, cursor = database_connect()

    sql = """SELECT race_id,
                    snail_id, 
                    snail_name, 
                    trainer_name 
             FROM fulldataview 
             WHERE race_id = ANY(ARRAY{});""".format(race_IDs)

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

    sql = "SELECT start_date FROM round WHERE closed = 'f' AND start_date > %s"

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

    query = "SELECT race_id, " \
            "       position, " \
            "       snail_name, " \
            "       trainer_name " \
            "FROM fulldataview " \
            "WHERE closed = 'f' AND position = 1"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return (cursor.fetchall())
