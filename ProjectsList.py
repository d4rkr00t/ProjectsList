# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import subprocess
import sys 
import os
import glob

class ProjectsListOpenCommand(sublime_plugin.WindowCommand):
	def run(self):
		show_select_projects(self)

	def selected(self, item):
		load_project(self, item, True, True)

class ProjectsListAppendCommand(sublime_plugin.WindowCommand):
	def run(self):
		show_select_projects(self)

	def selected(self, item):
		if item != -1:
			load_project(self, item, False, False)



# ========================================================
# 
# Shared methods
# 
# ========================================================

def load_project(self, item, clear_folders_list, open_on_start):
	#
	# Load project by selected id
	#
	if item != -1:

		if clear_folders_list:
			self.window.run_command('close_folder_list');

		for path in self.projects[item]['paths']:
			if sublime.platform() == "windows":
				project_path = u' -a '.join((self.subl_path, path)).encode('cp1251').strip()
			else:
				project_path = u' -a '.join((self.subl_path, path))

			print project_path

			subprocess.Popen(project_path, shell=True)

		if open_on_start:
			for f in self.projects[item]['open_on_start']:
				self.window.open_file(f)




def show_select_projects(self):
	#
	# Load projects list and show select popup
	#
	#Settings load:
	settings = sublime.load_settings('ProjectsList.sublime-settings')

	self.subl_path = get_sublime_path()

	if not self.subl_path:
		sublime.error_message("No Sublime path specified for current OS!")
		raise Exception("No Sublime path specified for current OS!")

	if settings.get('projects_'+sublime.platform()):
		self.projects = settings.get('projects_'+sublime.platform())
	else:
		sublime.error_message("No projects definde, goto Manage Projects!")
		raise Exception("No projects definde, goto Manage Projects!")		

	names = []

	for i in self.projects:
		names.append("%s" % (i["name"]))

	self.window.show_quick_panel(names, self.selected, sublime.MONOSPACE_FONT)

def get_sublime_path():
    if sublime.platform() == 'osx':
        return '/Applications/Sublime\\ Text\\ 2.app/Contents/SharedSupport/bin/subl'
    if sublime.platform() == 'linux':
        return open('/proc/self/cmdline').read().split(chr(0))[0]
    return sys.executable