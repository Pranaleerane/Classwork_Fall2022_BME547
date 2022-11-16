import tkinter as tk
from tkinter import ttk
import db_client


def create_blood_type(letter, rh):
    output = "{}{}".format(letter, rh)
    return output


def upload_data_to_server(patient_name, patient_id, patient_blood_letter,
                          patient_rh_factor):
    blood_type = create_blood_type(patient_blood_letter, patient_rh_factor)
    patient_id = int(patient_id)
    msg, code = db_client.upload_patient_info(patient_name,
                                              patient_id,
                                              blood_type)
    return msg


def main_window():


    def ok_cmd():
        if rh_button.get() == "":
            print ("choose a rh factor")
            return
        patient_name = patient_name_entry.get()
        patient_id = patient_id_entry.get()
        patient_blood_letter = blood_letter_selection.get()
        patient_rh_factor = rh_button.get()


    msg = upload_data_to_server(patient_name, patient_id, 
                                patient_blood_letter, patient_rh_factor)

    # Create new window to house all the interface.
    root = tk.Tk() 
    root.title("Blood Donor Database window")
    # makes the initial size of the window
    root.geometry("600x300")
    # this shriks the window so this fits.
    ttk.Label(root, text="Blood Donor Database").grid(column = 0,
                                                      row = 0)
    ttk.Label(root, text="Name").grid(column = 0, row = 1)
    ttk.Entry(root).grid(column = 1, row = 1, columnspan=2)

    patient_name_entry = tk.StringVar()
    ttk.Entry(root, width = 50, textvariable = patient_name_entry).grid(column = 1,
                                                                        row = 1)

    ttk.Label(root, text="Patient ID").grid(column = 0, row = 2)
    patient_id_entry = tk.StringVar()
    ttk.Entry(root, width = 50, textvariable = patient_id_entry).grid(column = 1,
                                                                      row = 2)


    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text = 'A', variable = blood_letter_selection,
                    value = 'A').grid(column = 0, row = 3)
    ttk.Radiobutton(root, text = 'B', variable = blood_letter_selection,
                    value = 'B').grid(column = 0, row = 4)
    ttk.Radiobutton(root, text = 'AB', variable = blood_letter_selection,
                    value = 'AB').grid(column = 0, row = 5)
    ttk.Radiobutton(root, text = 'O', variable = blood_letter_selection,
                    value = 'O').grid(column = 0, row = 6)


    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text = "Rh Positive",
                    variable=rh_button,
                    onvalue="+",
                    offvalue="-").grid(column=1, row=4)


# do not write the ok_cmd() with parenthesis because
    # # it will run the function immediately and not really execute it.
    ttk.Button(root, text = "OK", command = ok_cmd).grid(column = 1, row = 6)


    root.mainloop() # this starts the interface.


if __name__ == '__main__':
    main_window()