from scripts.main import  main
import os
data = {
    "userName":"unknown",
    "currentPath":"/"
}
while True:
    try:
        data = main(input(f"\n[ my-file@ {data['userName']}  {data['currentPath']}] :"), data)
    except KeyboardInterrupt:
        pass