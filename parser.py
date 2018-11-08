from sdev_py_utils import postgres_utils
from sdev_pandas_utils import to_sql
import pandas as pd
import os

engine = postgres_utils.get_engine("kamu-junction-vm4.kamu.gg", 32768)

rec_ids = pd.read_sql("select * from recording_session limit 10;", engine)

output_folder = 'data/'
for i in rec_ids.session_id:

    kills = pd.read_sql(
        f"select * from kills inner join(select * from recording_session where session_id = {i}) as recording_s on kills.killer_recording_id = recording_s.recording_id ",
        engine)

    deaths = pd.read_sql(
        f"select * from kills inner join(select * from recording_session where session_id = {i}) as recording_s on kills.victim_recording_id = recording_s.recording_id ",
        engine)

    damage_dealt = pd.read_sql(
        f"select * from damage inner join(select * from recording_session where session_id = {i}) as recording_s on damage.attacker_recording_id = recording_s.recording_id ",
        engine)

    damage_received = pd.read_sql(
        f"select * from damage inner join(select * from recording_session where session_id = {i}) as recording_s on damage.victim_recording_id = recording_s.recording_id ",
        engine)

    ticks = pd.read_sql(
        f"select * from ticks inner join(select * from recording_session where session_id = {i}) as recording_s on ticks.recording_id = recording_s.recording_id ",
        engine)

    weapon = pd.read_sql(
        f"select * from weapon inner join(select * from recording_session where session_id = {i}) as recording_s on weapon.recording_id = recording_s.recording_id ",
        engine)

    server_sessions = pd.read_sql(
        f"select * from server_session inner join(select * from recording_session where session_id = {i}) as recording_s on server_session.recording_id = recording_s.recording_id ",
        engine)

    player_sessions = pd.read_sql(
        f"select * from player_session inner join(select * from recording_session where session_id = {i}) as recording_s on player_session.recording_id = recording_s.recording_id ",
        engine)

    recording_sessions = pd.read_sql(
        f"select * from recording_session inner join(select * from recording_session where session_id = {i}) as recording_s on recording_session.recording_id = recording_s.recording_id ",
        engine)

    if not os.path.exists(output_folder + str(i)):
        os.makedirs(output_folder + str(i))

    kills.to_csv((output_folder + str(i) + '/kills.csv'))
    deaths.to_csv((output_folder + str(i) + '/deaths.csv'))
    damage_dealt.to_csv((output_folder + str(i) + '/damage_dealt.csv'))
    damage_received.to_csv((output_folder + str(i) + '/damage_received.csv'))
    ticks.to_csv((output_folder + str(i) + '/ticks.csv'))
    weapon.to_csv((output_folder + str(i) + '/weapon.csv'))
    server_sessions.to_csv((output_folder + str(i) + '/server_session.csv'))
    player_sessions.to_csv((output_folder + str(i) + '/player_session.csv'))
    recording_sessions.to_csv((output_folder + str(i) + '/recording_session.csv'))



