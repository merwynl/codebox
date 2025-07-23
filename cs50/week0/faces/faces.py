def convert(emotion):
    emotion = emotion.replace(":)", "🙂")
    emotion = emotion.replace(":(", "🙁")
    return emotion

def main():
    greeting = input()
    print(convert(greeting))

main()
