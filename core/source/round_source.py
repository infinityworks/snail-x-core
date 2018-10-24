from core.db.db_func import get_db
from core.repositories.round_repositry import get_current_round_race_results
from datetime import datetime


def get_open_round_id():
    db = get_db()
    cursor = db.cursor()

    current_time = datetime.now()
    args = (current_time, current_time)
    query = """SELECT round.round_id 
            FROM round JOIN race ON round.round_id = race.round_id 
            WHERE round.start_date <= '{}' 
            AND race.race_date >= '{}'""".format(current_time, current_time)

    try:
        # inserts the current date and time in to the above SQL query
        cursor.execute(query, args)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()


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

    return(cursor.fetchall())