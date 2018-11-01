from core.db.db_func import get_db
import datetime


def database_connect():
    db = get_db()
    cursor = db.cursor()
    return db, cursor


# returns round ID and name of currently-open round, as well as a list of race IDs for that round
def get_open_round():
    db, cursor = database_connect()

    current_time = datetime.datetime.now()

    args = (current_time,)

    sql = "SELECT DISTINCT round_id, round_name, race_id FROM fulldataview WHERE closed = false AND race_date > %s"

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
    db, cursor = database_connect()

    current_time = datetime.datetime.now()
    args = (current_time,)

    query = "SELECT round_id FROM fulldataview WHERE start_date < %s AND closed = false"

    try:
        cursor.execute(query, args)
        db.commit()
    except db.Error:
        return False

    round_id = cursor.fetchone()

    return round_id


# returns a list of objects, each of which contains a race id and a race_data object
# each of which specifies a snail id, snail name and trainer name of that snail
def get_round_snails(race_ids):
    db, cursor = database_connect()

    sql = """SELECT race_id,
                    snail_id, 
                    snail_name, 
                    trainer_name 
             FROM fulldataview 
             WHERE race_id = ANY(ARRAY{});""".format(race_ids)

    cursor.execute(sql)

    temp_races_dict = {}
    query_data = []

    for row in cursor:
        race_id = row[0]
        snail_id = row[1]
        snail_name = row[2]
        trainer_name = row[3]

        temp_snails_obj = {"snail_id": snail_id, "snail_name": snail_name, "trainer_name": trainer_name}

        if race_id in temp_races_dict:
            temp_races_dict[race_id].append(temp_snails_obj)
        else:
            temp_races_dict[race_id] = []
            temp_races_dict[race_id].append(temp_snails_obj)

    for race in temp_races_dict:
        race_obj = {"race_id": race, "race_data": temp_races_dict[race]}
        query_data.append(race_obj)

    return query_data


# Returns an object specifying a the round id and name of the current open round, as well as
# a list in the format returned by get_round_snails
def get_open_round_details():
    round_id, round_name, race_ids = get_open_round()
    races_snails_info = get_round_snails(race_ids)
    round_details = {"round_id": round_id, "round_name": round_name, "races": races_snails_info}

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


def get_future_round_details():
    db = get_db()
    cursor = db.cursor()

    current_time = datetime.datetime.now()
    args = str(current_time)

    sql = "SELECT start_date FROM round WHERE closed = false AND start_date > %s"

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
    db, cursor = database_connect()

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

    return cursor.fetchall()


def get_all_closed_round_names():
    db, cursor = database_connect()

    query = "select round_name from round where closed = TRUE order by round_name asc "

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()


def find_one_by_name(round_name):
    db, cursor = database_connect()

    query = "select round_id from round where round_name = \'" + str(round_name) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchone()
