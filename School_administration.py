import csv
def write_csv(sinfo_list):
    with open('Student_info.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-Mail ID"])
        writer.writerow(sinfo_list)
def search_string_in_file(string_to_search):
    serial_number = -1
    list_of_results = []
    with open('Student_info.csv', 'r') as read_obj:
        for line in read_obj:
            serial_number += 1
            if string_to_search in line:
                list_of_results.append((serial_number, line.rstrip()))
    return list_of_results
condition = True
con = True
snum = 1
while(con):
    check = input("Do You Want to Enter Information or Do You Want to Read Information or Do You Want to Seach a Particular Student! (enter/read/search):")
    if check == "enter":
        while(condition):
            student_info = input("\nEnter the Student Information for student #{} in the following format [Name Age Contact_number Email_ID]: " .format(snum))
            student_list = student_info.split(' ')
            if len(student_list[2]) == 10:
                if "@" in student_list[3] and "." in student_list[3]:
                    print("\nThe Entered Information is - \nName: {}\nAge: {} \nContact Number: {} \nE-Mail ID: {}\n"
                                      .format(student_list[0], student_list[1], student_list[2], student_list[3]))
                    choice_check = input("\nIs the Entered Student Information Correct? (yes/no): ")
                    if choice_check == "yes":
                        write_csv(student_list)
                        c_check = input("\nEnter (yes/no) if you want to enter Information for another student: ")
                        if c_check == "yes":
                            condition = True
                            snum = snum + 1
                        elif c_check == "no":
                            condition = False
                            reenter = input("\nDo You want to Read or Search Student Information now! (yes/no): ")
                            if reenter == "yes":
                                print("\nPlease Select \"read\" or \"search\" respectively to so\n")
                                con = True
                                condition = True
                            else:
                                print("Thank You")
                                con = False
                    elif choice_check == "no":
                        print("\n Please re-enter Student Information!\n")
                else:
                    print("\n Please re-enter Student Information with correct Email ID!\n")
            else:
                print("\n Please Re-enter Student Information with correct contact Number!\n ")
    elif check == "read":
        print("\nAll the Student Information Registered Till Now is as follows: ")
        read = open("Student_info.csv", "r")
        for x in read:
            print(x)
        reenter1 = input("\nDo You want to Enter or Search Student Information now! (yes/no): ")
        if reenter1 == "yes":
            print("\nPlease Select \"enter\" or \"search\" respectively to do so\n")
            con = True
            condition = True
        else:
            print("Thank You")
            con = False           
    elif check == "search":
        contact = input("\nPlease Enter the Contact number of the student to be checked: ")
        matched_lines = search_string_in_file(contact)
        print('\nTotal Number of Student found : ', len(matched_lines))
        for elem in matched_lines:
            elem_list = elem[1].split(',')
            print("\nStudent Information with serial number {}" .format(elem[0]))
            print("\nThe Entered Information is - \nName: {}\nAge: {} \nContact Number: {} \nE-Mail ID: {}\n"
                        .format(elem_list[0], elem_list[1], elem_list[2], elem_list[3]))        
        reenter2 = input("\nDo You want to Read or Enter Student Information now! (yes/no): ")
        if reenter2 == "yes":
            print("\nPlease Select \"enter\" or \"read\" respectively to do so\n")
            con = True
            condition = True
        else:
            print("Thank You")
            con = False
