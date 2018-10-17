from core.db.db_func import get_db
import datetime


def get_open_round():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    args = current_time, current_time
    #args = ('2018-10-15 12:00:00', '2018-10-15 12:00:00')

    sql = """SELECT round.roundid, round.roundname, race.raceid 
            FROM round JOIN race ON round.roundid = race.roundid 
            WHERE round.start <= %s 
            AND race.racedate >= %s"""

    cursor.execute(sql, args)

    raceIDs = []
    first_row = cursor.fetchone()
    round_ID = first_row[0]
    round_name = first_row[1]

    for record in cursor:
        raceIDs.append(record[2])

    #round_data = {"round_id": round_ID, "round_name": round_name, "race_IDs": raceIDs}

    return round_ID, round_name, raceIDs
    #return round_data


def get_round_snails(race_IDs):
    db = get_db()
    cursor = db.cursor()

    sql = """SELECT racecard.raceid, snails.snailid, snails.name AS snailName, trainers.name AS trainerName 
            FROM racecard JOIN snails ON racecard.snailID = snails.snailID 
            JOIN trainers ON snails.trainerID = trainers.trainerID 
            WHERE racecard.raceid = ANY(%s);"""

    cursor.execute(sql, (race_IDs,))

    query_data = {}

    for row in cursor:
        raceid = row[0]
        snailid = row[1]
        snailname = row[2]
        trainername = row[3]

        if raceid in query_data: # if snails for a particular race have already started being entered
            races_dict = query_data[raceid] # get the already-created race dictionary for those snails
        else:
            races_dict = {}

        races_dict[snailid] = (snailname, trainername)
        query_data[raceid] = races_dict

    return query_data


def get_open_round_details():
    round_ID, round_name, race_IDs = get_open_round()
    races_snails_info = get_round_snails(race_IDs)
    round_details = {"roundid": round_ID, "roundname": round_name, "races": races_snails_info}

    return round_details





