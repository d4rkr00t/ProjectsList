# ProjectsList
Simple Projects List for Sublime Text 2

## Overview

This plugin allow define your most used folders sets in projects with fast access for it.

You may also define files in project openes on startup.

ProjectsList plugin allow you open single project or append any defined projects to alredy opened.

## Installation
Note with either method, you may need to restart Sublime Text 2 for the plugin to load.

### Package Control
// TODO: Add to Package Control

### Manual
Clone git repo to Sublime packages dir.

	git clone https://github.com/d4rkr00t/ProjectsList.git ProjectsList

## Usage
Before use this plugin you must define projects in settings. Call "Manage Projects" from command palette. 

Projects list format:

	{
		// "projects_windows": [
			// {
			// 	"name":"Project Name", 
			// 	"paths": ["folder append", "second folder append", ...], 
			// 	"open_on_start": ["file opened on start", "second file append on start", ...]
			// },
		// ],
		// "projects_linux": [
			// {
			// 	"name":"Project Name", 
			// 	"paths": ["folder append", "second folder append", ...], 
			// 	"open_on_start": ["file opened on start", "second file append on start", ...]
			// },
		// ],
		// "projects_osx": [
			// {
			// 	"name":"Project Name", 
			// 	"paths": ["folder append", "second folder append", ...], 
			// 	"open_on_start": ["file opened on start", "second file append on start", ...]
			// },
		// ]
	}

And then you may call command "Open prject" or "Append Project" from command palette.