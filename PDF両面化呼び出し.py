import appex
import PDF両面化

print(appex.is_running_extension())

file_paths = appex.get_file_paths()

for i,file_path in enumerate(file_paths):
	print(i)
	print(file_path)
	PDF両面化.main(file_path)
