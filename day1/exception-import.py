try:
	import special_module
except ImportError:
        print("Sorry, you don't have the special_module installed,")
        print("and this program relies on it.")
        print("Please install or reconfigure special_module and try again.")
