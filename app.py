import glob
import pandas as pd
import re
import subprocess
import os
import argparse
from pathlib import Path

CHAT_PATH = "./discord_chats/"
RESULT_PATH = "./out/"

def read_config():
    import yaml
    with open("config.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# searches in a directory for a file with a specified channel_id, returns dataframe
def read_csv(channel_id="", path=""):
    if not path:
        if not channel_id:
            channel_id = read_config()['channel_id']
        found_files = glob.glob(f"{CHAT_PATH}*{channel_id}*.csv")
        if(len(found_files) < 1):
            raise ValueError(f"could not find file with channel id: {channel_id} at path: {CHAT_PATH}")
        if(len(found_files) > 1):
            raise ValueError(f"multiple files found with channel id: {channel_id} at path: {CHAT_PATH}")
        return pd.read_csv(f'{found_files[0]}', sep=',')
    else:
        found_files = glob.glob(f"{path}")
        return pd.read_csv(f'{found_files[0]}', sep=';')       

def replace_names(df):
    # df.drop(columns="Autor", inplace=True)
    roles = read_config()['roles'] # dictionary of key: list
    for role_item in roles.items():
        role = role_item[0]
        names_array = role_item[1]
        for name in names_array:
            re_replace_author_content = re.compile(re.escape(name), re.IGNORECASE)
            re_remove_discord_tag = r"#\d{4}"
            df['Inhalt'].replace(to_replace=re_replace_author_content, value=f"{role}", inplace=True, regex=True)
            df['Autor'].replace(to_replace=re_replace_author_content, value=f"{role}", inplace=True, regex=True)
            df['Autor'].replace(to_replace=re_remove_discord_tag, value=f"", inplace=True, regex=True)
    return df

def main(): 
    config = read_config()
    channel_id = config['channel_id']
    token = config['token']

    parser = argparse.ArgumentParser()
    parser.add_argument('-c',"--csv", type=str,help="if provided will replace for a `csv` file")
    args = parser.parse_args()

    if args.csv is not None:
        csv_path = Path(args.csv)
        filename = os.path.basename(csv_path)
        df = read_csv(path=args.csv)
        df = replace_names(df)
        df.to_csv(f'{RESULT_PATH}/{filename}', index=False)
    else:
        with open("logs/DiscordChatExporterCLI.log", "a") as output:
            subprocess.call(
                f"DiscordChatExporter\\DiscordChatExporter.Cli.exe export -o ./discord_chats -t {token} -c {channel_id} -f CSV",
                shell=True,
                stdout=output,
                stderr=output
            )
            df = read_csv()
            df = replace_names(df)
            df.to_csv(f'{RESULT_PATH}{channel_id}.csv', index=False)

main()