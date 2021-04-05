from distutils.core import setup
import py2exe

def ytdl():
    import pafy, os, re, urllib,glob, subprocess
    setup(
        console = [
            {
                "script": "ytdl.py",
                "icon_resources": [(1, "yt.ico")]
            }
        ]
    )
ytdl()