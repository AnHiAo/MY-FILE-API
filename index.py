from scripts.main import  main
data = {
    "userName":"nio",
    "currentPath":"/"
}
while True:
    try:
        data = main(input(f"\n[ my-file@ {data['userName']}  {data['currentPath']}] :"), data)
    except KeyboardInterrupt:
        pass