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

			subprocess.Popen(project_path)

		if open_on_start:
			for f in self.projects[item]['open_on_start']:
				self.window.open_file(f)




def show_select_projects(self):
	#
	# Load projects list and show select popup
	#
	#Settings load:
	settings = sublime.load_settings('ProjectsList.sublime-settings')

	self.subl_path = sys.executable

	if not self.subl_path:
		sublime.error_message("No Sublime path specified for current OS!")
		raise Exception("No Sublime path specified for current OS!")

	try:
		with open(self.subl_path) as f: pass
	except IOError as e:
		sublime.error_message("Wrong Sublime path!")
		raise Exception("Wrong Sublime path!")

	if settings.get('projects_'+sublime.platform()):
		self.projects = settings.get('projects_'+sublime.platform())

	names = []

	for i in self.projects:
		names.append("%s" % (i["name"]))

	self.window.show_quick_panel(names, self.selected, sublime.MONOSPACE_FONT)