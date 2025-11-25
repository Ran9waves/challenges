from attackcti import attack_client
import pandas as pd
import json

lift = attack_client()

class MITREAttackReporter:
    def __init__(self,lift_client):
        self.lift = lift_client
    
    def get_groups(self,export_format):
        groups = self.lift.get_groups()
        print("Number of ATT&CK Groups:",len(groups))
        groups_list = [json.loads(g.serialize())for g in groups]
        self.export_data(groups_list, "mitre_groups", export_format)

    def export_data(self,data,filename,export_format):
        if export_format == "excel":
            df = pd.json_normalize(data)
            df.to_excel(f"{filename}.xlsx",index=False)
            print(f"Report exported to: {filename}.xlsx")

reporter = MITREAttackReporter(lift)
reporter.get_groups("excel")