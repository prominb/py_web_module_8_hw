from hw1 import find_by_author, find_by_tag


def main():
    check_loop_status = True
    while check_loop_status:
        user_input = input("Input command ([name: Author name] or [tag:life] or Exit): ")
        check_conditions = user_input.strip().split(':', 1)
        if user_input.lower() == "exit":
            print("Good by!")
            check_loop_status = False
        elif check_conditions[0].startswith("name"):
            normalize_author = check_conditions[1].strip()
            print(find_by_author(normalize_author))
        elif check_conditions[0] == "tag":  # check_conditions[0].startswith("tag"):
            normalize_tag = check_conditions[1].strip()
            print(find_by_tag(normalize_tag))
        elif check_conditions[0] == "tags":  # check_conditions[0].startswith("tags"):
            normalize_tags = check_conditions[1].strip().split(',')
            # print(normalize_tags)
            for tg in normalize_tags:
                print(find_by_tag(tg))


if __name__ == '__main__':
    main()

# name: Albert Einstein OR name: Steve Martin
# name:st OR name:stev OR name:stei
# tag:life OR tag:li
# tags:life,live
