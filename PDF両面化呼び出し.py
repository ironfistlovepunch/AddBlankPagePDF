import appex
import PDF両面化

print(appex.is_running_extension())
print(appex.get_text())

file_path = appex.get_file_path()
print(file_path)
PDF両面化.main(file_path)
