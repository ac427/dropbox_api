#!/usr/bin/env python

import dropbox
import ConfigParser


Config = ConfigParser.ConfigParser()
Config.read("config")

#dbx = dropbox.Dropbox('YOUR_ACCESS_TOKEN')
DROPBOX_TOKEN=Config.get ("config", "DROPBOX_TOKEN")
dbx = dropbox.Dropbox(DROPBOX_TOKEN)
print dbx.users_get_current_account()

#list
#for entry in dbx.files_list_folder('').entries:
#    print(entry.name)

#entries; dropbox has no support to upload dir. https://github.com/dropbox/dropbox-sdk-python/issues/107
#dbx.files_upload("Potential headline: Game 5 a nail-biter as Warriors inch out Cavs", '/cavs vs warriors/game 5/story.txt')
#dbx.files_upload('file_to_upload','location_in_dropbox_app_dir')
dbx.files_upload('here.txt','/ac_foo/here.txt')

#print metadata
#print(dbx.files_get_metadata('/ac_foo/here.txt').server_modified)

