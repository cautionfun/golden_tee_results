##filter results
##import pandas
import pandas as pd
##loads in the compiled results
results = pd.read_csv("final/combined_csv.csv")
##filters for course and game mode and saves each row that returns TRUE as a variable
##'98 Speed Runs
sr_ah = results[(results["course"] == 'Arbor Hill') & (results["mode"] == 'Speed Run')]
sr_bb = results[(results["course"] == 'Bayou Bend') & (results["mode"] == 'Speed Run')]
sr_pg = results[(results["course"] == 'Palm Grove') & (results["mode"] == 'Speed Run')]
##'99 Speed Runs
sr_al = results[(results["course"] == 'Aspen Lake') & (results["mode"] == 'Speed Run')]
sr_cc = results[(results["course"] == 'Coconut Cove') & (results["mode"] == 'Speed Run')]
sr_rs = results[(results["course"] == 'Rancho Saguaro') & (results["mode"] == 'Speed Run')]
##2k Speed Runs
sr_sv = results[(results["course"] == 'Stone Valley') & (results["mode"] == 'Speed Run')]
sr_sh = results[(results["course"] == 'Sea Haven') & (results["mode"] == 'Speed Run')]
sr_cr = results[(results["course"] == 'Coyote Run') & (results["mode"] == 'Speed Run')]
##Classic Speed Runs
sr_ms = results[(results["course"] == 'Mountain Springs') & (results["mode"] == 'Speed Run')]
sr_ac = results[(results["course"] == 'Anchor Cove') & (results["mode"] == 'Speed Run')]
sr_sb = results[(results["course"] == 'Scorpian Bend') & (results["mode"] == 'Speed Run')]
##SKINS
##//skins = results.loc[(results["mode"] == 'Skins'), ("mode", "player", "winnings")]
##now we send the filtered variables to their appropriate folders, each as their own csv file
##'98
sr_ah.to_csv("final/SpeedRun/98/ArborHill.csv", index=False, encoding='utf-8-sig')
sr_bb.to_csv("final/SpeedRun/98/BayouBend.csv", index=False, encoding='utf-8-sig')
sr_pg.to_csv("final/SpeedRun/98/PalmGrove.csv", index=False, encoding='utf-8-sig')
##'99
sr_al.to_csv("final/SpeedRun/99/AspenLake.csv", index=False, encoding='utf-8-sig')
sr_cc.to_csv("final/SpeedRun/99/CoconutCove.csv", index=False, encoding='utf-8-sig')
sr_rs.to_csv("final/SpeedRun/99/RanchoSaguaro.csv", index=False, encoding='utf-8-sig')
##2k
sr_sv.to_csv("final/SpeedRun/2k/StoneValley.csv", index=False, encoding='utf-8-sig')
sr_sh.to_csv("final/SpeedRun/2k/SeaHaven.csv", index=False, encoding='utf-8-sig')
sr_cr.to_csv("final/SpeedRun/2k/CoyoteRun.csv", index=False, encoding='utf-8-sig')
##Classic
sr_ms.to_csv("final/SpeedRun/Classic/MountainSprings.csv", index=False, encoding='utf-8-sig')
sr_ac.to_csv("final/SpeedRun/Classic/AnchorCove.csv", index=False, encoding='utf-8-sig')
sr_sb.to_csv("final/SpeedRun/Classic/ScorpianBend.csv", index=False, encoding='utf-8-sig')
##SKINS
##//skins.to_csv("final/Skins/skins.csv", index=False, encoding='utf-8-sig')
