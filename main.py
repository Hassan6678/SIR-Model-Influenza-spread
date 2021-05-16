'''
USA Total Population (N) = 60,000   R (0) = 0
Netherlands Total Population (N) = 5,000    R (0) = 0
Rages β = [0.00, 1.00] γ = [0.00, 1.00] t = [0.00, 1.00]
Granularities Δβ = 0.01 Δγ = 0.01 Δt = 0.1
'''

'''
dS = -β I S * Δt
dR = γ I  * Δt
dI = (β I S - γ I) * Δt
'''

def Data_set_2009_2010():
    USA_total_population = 60000
    NL_total_population = 5000
    USA_root_mean_sq_err = []
    NL_root_mean_sq_err = []
    beta_value = []
    gema_value = []

    USA_logical_pro = True
    NL_logical_pro = True

    # Read data-set file
    f = open("data_set_2009_2010.txt", "r")
    Sr_No = []
    year = []
    Week = []
    USA_I = []
    NL_I = []
    for x in f:
        data = (x.split())
        Sr_No.append(data[0])
        year.append(data[1])
        Week.append(data[3])
        USA_I.append(data[4])
        NL_I.append(data[5])

    # Using Data-Set of Influenza spread data set in USA and Netherlands during 2009-2010
    file_count = 1
    for beta in range(1,101): # Value start from 0.01
        #print(beta/100, end="")
        for gema in range(1,101): # Value start from 0.01

            '''
            Create a New Text file for Each Trace
            '''
            #file = open(str(file_count) + '_log.txt', 'w+')
            #file_count += 1;


            #file.write("Beta : " + str(beta/100) + "\t" + "gema : " + str(gema/ 100)+"\n")

            error_sum_usa = 0
            error_sum_nl = 0

            for time in range(55): # count for Week in data-set
                # We wanna make a traces file on this simulation, So ...
                # Calculate value of S for USA and NL

                USA_S = USA_total_population - float(USA_I[time])
                NL_S = NL_total_population - float(NL_I[time])

                I_for_USA = (((beta/100) * float(USA_I[time]) * float(USA_S) ) - ((gema/100) * float(USA_I[time])) ) * ((time+1)/100)

                '''
                Logical Properties
                Infected population at time t not greater then total population
                '''
                if I_for_USA > USA_total_population:
                    I_for_USA = USA_total_population
                    USA_logical_pro = False


                I_for_NL = (((beta / 100) * float(NL_I[time]) * float(NL_S)) - ((gema / 100) * float(NL_I[time]))) * ((time+1) / 100)

                '''
                Logical Properties
                Infected population at time t not greater then total population
                '''
                if I_for_NL > NL_total_population:
                    I_for_NL = NL_total_population
                    NL_logical_pro = False

                # change_S_usa = -1 * ( beta / 100 * float(USA_I[time]) * USA_S ) * (time+1) / 100
                # change_S_nl = -1 * (beta / 100 * float(NL_I[time]) * NL_S) * (time + 1) / 100

                '''
                Export trace in some text/excel file
                '''
                #file.write(str(time+1)+"\t"+str(year[time])+"\tweek: "+Week[time]+"\t"+str(int(I_for_USA))+"\t"+str(int(I_for_NL))+"\n")


                #Now I wanna to check Root Mean Square Error (RMSR)
                # Formula : Sigma_limit (1-N) (Empirical value - obtain value ) ^ 2 / N

                #print((float(USA_I[time]) - I_for_USA ) ** 2)
                error_sum_usa += (float(USA_I[time]) - I_for_USA ) ** 2
                error_sum_nl += (float(NL_I[time]) - I_for_NL) ** 2

            # end For loop for time
            RMSE_USA = error_sum_usa / time+1
            #print("ROOT MEAN SQUARE ERROR USA ",RMSE_USA ** 0.5)
            USA_root_mean_sq_err.append(RMSE_USA ** 0.5)

            RMSE_NL = error_sum_nl / time + 1
            #print("ROOT MEAN SQUARE ERROR NL", RMSE_NL ** 0.5)
            NL_root_mean_sq_err.append(RMSE_NL ** 0.5)

            # append beta and gema value ...
            beta_value.append(beta/100)
            gema_value.append(gema/100)


    beta_tune, gema_tune, USA_tune, NL_tune =_1_age_value(beta_value, gema_value, USA_root_mean_sq_err, NL_root_mean_sq_err)

    print("\nLogicl Property for USA: ", USA_logical_pro)
    print("Logical Property for NL: ", NL_logical_pro)
    print("\n")

    return beta_tune, gema_tune, USA_tune, NL_tune


def _1_age_value(beta_value, gema_value, USA_root_mean_sq_err, NL_root_mean_sq_err):
    beta_tune = []
    gema_tune = []
    USA_tune = []
    NL_tune = []

    # 1 %
    one_percentage = len(USA_root_mean_sq_err) * 0.01
    print(one_percentage)

    for k in range(int(one_percentage)):
        # Find smallest value's index in list
        index = USA_root_mean_sq_err.index(min(USA_root_mean_sq_err))
        inx = NL_root_mean_sq_err.index(min(NL_root_mean_sq_err))

        if (index == inx):
            beta_tune.append(beta_value.pop(index))
            gema_tune.append(gema_value.pop(index))
            USA_tune.append(USA_root_mean_sq_err.pop(index))
            NL_tune.append(NL_root_mean_sq_err.pop(index))

    return beta_tune, gema_tune, USA_tune, NL_tune


def data_set_2010_2011():
    beta_tune, gema_tune, USA_tune, NL_tune = Data_set_2009_2010()

    #print(beta_tune)
    USA_total_population = 60000
    NL_total_population = 5000
    USA_root_mean_sq_err = []
    NL_root_mean_sq_err = []

    # Read data-set file
    f = open("data_set_2010_2011.txt", "r")
    Sr_No = []
    year = []
    Week = []
    USA_I = []
    NL_I = []
    for x in f:
        data = (x.split())
        Sr_No.append(data[0])
        year.append(data[1])
        Week.append(data[3])
        USA_I.append(data[4])
        NL_I.append(data[5])


    # Now for loop on tuning beta gema value ....
    for i in range(len(beta_tune)):
        error_sum_usa = 0
        error_sum_nl = 0

        for time in range(55):  # count for Week in data-set
            # We wanna make a traces file on this simulation, So ...
            # Calculate value of S for USA and NL

            # USA_S = total_usa + change_S_usa
            # NL_S = total_nl + change_S_nl
            USA_S = USA_total_population - float(USA_I[time])
            NL_S = NL_total_population - float(NL_I[time])

            # NOw We Make a txt file on each trace

            # dI = (β I S - γ I) * Δt

            #print("value of Beta : ",beta_tune[i])
            #print("value of Gema : ", gema_tune[i])
            #print("Value of USA_I : ",float(USA_I[time]))
            #print("Value of USA_S",float(USA_S))
            #print("time : : : ", time)
            #print("timeValue : ",(time + 1) / 100)


            I_for_USA = (((beta_tune[i]) * float(USA_I[time]) * float(USA_S)) - ((gema_tune[i]) * float(USA_I[time]))) * (
                    (time + 1) / 100)

            '''
            Logical Properties
            Infected population at time t not greater then total population
            '''
            if I_for_USA > USA_total_population:
                I_for_USA = USA_total_population

            I_for_NL = (((beta_tune[i]) * float(NL_I[time]) * float(NL_S)) - ((gema_tune[i]) * float(NL_I[time]))) * (
                (time + 1) / 100)

            '''
            Logical Properties
            Infected population at time t not greater then total population
            '''
            if I_for_NL > NL_total_population:
                I_for_NL = NL_total_population

            # dS = -β I S * Δt
            # change_S_usa = -1 * ( beta / 100 * float(USA_I[time]) * USA_S ) * (time+1) / 100
            # change_S_nl = -1 * (beta / 100 * float(NL_I[time]) * NL_S) * (time + 1) / 100

            # Text file format
            # file.write(str(time+1)+"\t"+str(year[time])+"\tweek: "+Week[time]+"\t"+str(int(I_for_USA))+"\t"+str(int(I_for_NL))+"\n")

            # Now I wanna to check Root Mean Square Error (RMSR)
            # Formula : Sigma_limit (1-N) (Empirical value - obtain value ) ^ 2 / N

            error_sum_usa += (float(USA_I[time]) - I_for_USA) ** 2
            error_sum_nl += (float(NL_I[time]) - I_for_NL) ** 2

        # end For loop for time
        RMSE_USA = error_sum_usa / (time + 1)
        USA_root_mean_sq_err.append(RMSE_USA ** 0.5)

        RMSE_NL = error_sum_nl / (time + 1)
        NL_root_mean_sq_err.append(RMSE_NL ** 0.5)


    #print(USA_root_mean_sq_err)
    #print(NL_root_mean_sq_err)

    return USA_root_mean_sq_err, NL_root_mean_sq_err



print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
print("<~~~~~~~~~~~~~~~~~~~Welcome to SIR MoDel~~~~~~~~~~~~~~~~~~~~>")
print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

print("Select your choice as follows:")
print("1. Please press '1' for getting tuning parameters (Data-set 2009-2010)")
print("2. Please press '2' for Model Prediction (Data-set 2010-2011)")

print("\n Press '0' Exit")

choice  = int(input("Enter your choice : "))

while (choice != 0):
    if choice == 1:
        beta_tune, gema_tune, USA_training_error, NL_training_error = Data_set_2009_2010()
        print("Beta Tune Value: ",beta_tune)
        print("Gema Tune Value: ", gema_tune)
        print("USA Training Error: ", USA_training_error)
        print("NL Training Error: ",NL_training_error)

    elif choice == 2:
        USA_testing_error , NL_testing_error = data_set_2010_2011()
        print("USA Testing Error : ", USA_testing_error)
        print("NL Testing Error: ", NL_testing_error)

    else:
        print("\nyou Enter Wrong, please try again.\n")

    print("Select your choice as follows:\n")
    print("1. Please press '1' for getting tuning parameters (Data-set 2009-2010)")
    print("2. Please press '2' for Model Prediction (Data-set 2010-2011)")

    print("\nPress '0' Exit\n")

    choice = int(input("Enter your choice : "))