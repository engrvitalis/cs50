"""
This project implements a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

"""

def main():

	#prompt the user for the name of a file
	f = input("Enter file name: ").lower().strip()
	e = f[-3:]

	#outputs that file’s media type
	match e:
		case "gif":
			print("image/gif")
		case "jpg" | "jpeg":
			print("image/jpeg")
		case "png":
			print("image/png")
		case "pdf":
			print("application/pdf")
		case "txt":
			print("text/plain")
		case "zip":
			print("application/zip")
		case _:
			print("application/octet-stream")


main()