def main():
    faces=input()
    f=convert(faces)
    print(f)
def convert(faces):
    faces1=faces.replace(":)", '🙂')
    faces2=faces1.replace(":(", '🙁')
    return faces2

main()