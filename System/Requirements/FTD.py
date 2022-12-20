dev_message = f'''
[]+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+[]
[]Hey guys! Here's the news for today! |issue: 1|[]
[]                              Date: 12-13-2022 []
[]+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+[]
[] [v1.2.2]      System Updates:                 []
[]                                               []
[]A whole whack of things have been updated and  []
[] changed! Check out the tree at the bottom!    []
[]+=+=+=+=+=+=+=+=+=+=+=+++=+=+=+=+=+=+=+=+=+=+=+[]
[]The 5 Best Uses (So Far) for ChatGPT's AI      []
[]Chatbot.                                       []
[]                                               []
[]There are several ways ChatGPT can make life   []
[]easier. The AI can be used to help people lower[]
[]bills, create diet and workout plans, help with[]
[]meal planning and grocery shopping, create     []
[]stories, and prepare for interviews. ChatGPT   []
[]still isn't perfect, as it isn't able to       []
[]separate fact from fiction. Its potential for  []
[]inaccuracy has caused it to be temporarily     []
[]banned from StackOverflow.                     []
[]+=+=+=+=+=+=+=+=+=+=+=+++=+=+=+=+=+=+=+=+=+=+=+[]
# Feature Tree!
⁃	Cache
⁃		Clear all git -> wipes all GitHub download data *Requires password
⁃	Settings
⁃		User
⁃			None
⁃		System
⁃			ForcedLogin *requires password
⁃				Toggles the need for a password on launch 
⁃			ForcedModuleImport *requires password
⁃				Toggles imports on launch
⁃	PackageInstaller
⁃		GitRepo
⁃			enter the git repo to clone -> 
⁃			    If using complicated install -> 
⁃			        enter all needed -> for (Permison Arguments) just enter the whole command 
⁃				for launch script, enter the corresponding number (check the repo for launch info)
⁃		LocalDir
⁃			enter the directory you want to connect
⁃				for launch script, enter the corresponding number
⁃	PackageActivator
⁃		GitHub
⁃			select the package to run from list
⁃		local
⁃			select the package to run from list
⁃		Complex-git
⁃			select the package to run from list
⁃	PackageUninstaller * will delete directory as well as launch command
⁃		Github
⁃			select the package to uninstall from list
⁃		Local
⁃			select the package to uninstall from list
⁃	Events/errors
⁃		all saved in System/Cache/System/ErrorLog/
[]+=+=+=+=+=+=+=+=+=+=+=+++=+=+=+=+=+=+=+=+=+=+=+[]
'''
Version = 'i1 : v1.2.2'
