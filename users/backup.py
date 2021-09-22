for p in cp:
        for i in range(6, 18):
            for j in range(1, 4):
                if j == 1:
                    if i < 10:
                        time = "0"+str(i)+":00:00"
                    else:
                        time = str(i)+":00:00"
                elif j == 2:
                    if i < 10:
                        time = "0"+str(i)+":20:00"
                    else:
                        time = str(i)+":20:00"
                else:
                    if i < 10:
                        time = "0"+str(i)+":40:00"
                    else:
                        time = str(i)+":40:00"
                if slots:
                    t = {"time":time,
                        "status":"not booked",
                        "point":p.point_number }
                    for slot in slots:
                        print(slot.charge_point_number, slot.slot_booked_time)
                        if slot.charge_point_number == p.point_number:
                            if time == str(slot.slot_booked_time):
                                t['status'] = "booked"
                                t['point'] = slot.charge_point_number
                                break
                            else:
                                continue
                    time_slots.append(t)
                else:
                    time_slots.append({
                            "time":time,
                            "status":"not booked",
                            "point":None
                        })