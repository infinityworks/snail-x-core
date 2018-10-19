from core.db.db_func import get_db
import datetime


def get_open_round():   # Returns the round_id, round_name oof the current open round, as well as a list of the race_ids of the races
                        # in that round
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    args = (current_time, current_time)

    sql = """SELECT round.round_id, round.round_name, race.race_id 
            FROM round JOIN race ON round.round_id = race.round_id 
            WHERE round.start_date <= %s 
            AND race.race_date >= %s"""

    cursor.execute(sql, args)   # inserts the current date and time iin to the above SQL query

    raceIDs = []
    round_ID = 0
    round_name = ""

    for record in cursor:   # Adds the each race ID to a list of raceIDs, and updates round Idd and round_name to that of the relevant round
        raceIDs.append(record[2])
        round_ID = record[0]
        round_name = record[1]

    return round_ID, round_name, raceIDs


def get_round_snails(race_IDs): # returns a list of objects, each of which contains a race id and a race_data object, each of
                                # each of which specifies a snail id, snail name and trainer name of that snail

    db = get_db()
    cursor = db.cursor()

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


def get_open_round_details():   # Returns an object specifying a the round id and name of the current open round, as well as
                                # a list in the format returned by get_round_snails
    round_ID, round_name, race_IDs = get_open_round()
    races_snails_info = get_round_snails(race_IDs)
    round_details = {"round_id": round_ID, "round_name": round_name, "races": races_snails_info}

    return round_details


def store_predictions(user_id, race_predictions):   # Inserts the user's predictions in to the racepredictions table
    db = get_db()
    cursor = db.cursor()
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






