import pandas as pd
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")

mathsScore = df["math score"].tolist()
readingScore = df["reading score"].tolist()
writingScore = df["writing score"].tolist()


def Mean_Median_Mode():
    # Mean
    mathsMean = st.mean(mathsScore)
    readingMean = st.mean(readingScore)
    writingMean = st.mean(writingScore)


    # Median
    mathsMedian = st.median(mathsScore)
    readingMedian = st.median(readingScore)
    writingMedian = st.median(writingScore)


    # Mode
    mathsMode = st.mode(mathsScore)
    readingMode = st.mode(readingScore)
    writingMode = st.mode(writingScore)


    # Standerd Diviation
    mathsStd = st.stdev(mathsScore)
    readingStd = st.stdev(readingScore)
    writingStd = st.stdev(writingScore)


    print('\n Mean of Maths Score: ', mathsMean, '\n', 'Mean of Reading Score: ',
          readingMean, '\n', 'Mean of Writing Score: ', writingMean)

    print('\n Median of Maths Score: ', mathsMedian, '\n', 'Median of Reading Score: ',
          readingMedian, '\n', 'Median of Writing Score: ', writingMedian)

    print('\n Mode of Maths Score: ', mathsMode, '\n', 'Mode of Reading Score: ',
          readingMode, '\n', 'Mode of Writing Score: ', writingMode)

    print('\n Standerd deviation of Maths Score: ', mathsStd, '\n', 'Standerd deviation of Reading Score: ',
          readingStd, '\n', 'Standerd deviation of Writing Score: ', writingStd)




    # Maths

    sd1_Start, sd1_End = mathsMean - mathsStd, mathsMean + mathsStd
    sd2_Start, sd2_End =  mathsMean - (2* mathsStd),  mathsMean + (2* mathsStd)
    sd3_Start, sd3_End =  mathsMean - (3* mathsStd),  mathsMean + (3* mathsStd)

    M_counterStd1 = 0
    M_counterStd2 = 0
    M_counterStd3 = 0

    for i in range(0, len(mathsScore)):
        value = mathsScore[i]
        if value >= sd1_Start and value <= sd1_End:
            M_counterStd1 += 1

        if value >= sd2_Start and value <= sd2_End:
            M_counterStd2 += 1

        if value >= sd3_Start and value <= sd3_End:
            M_counterStd3 += 1


    M_perOfSd1 = (M_counterStd1*100)/len(mathsScore)
    M_perOfSd2 = (M_counterStd2*100)/len(mathsScore)
    M_perOfSd3 = (M_counterStd3*100)/len(mathsScore)

    print('\n Maths Std1: ',M_perOfSd1)
    print(' Maths Std2: ',M_perOfSd2)
    print(' Maths Std3: ',M_perOfSd3)



    # Reading Score

    sd1_Start, sd1_End = readingMean - readingStd, readingMean + readingStd
    sd2_Start, sd2_End =  readingMean - (2* readingStd),  readingMean + (2* readingStd)
    sd3_Start, sd3_End =  readingMean - (3* readingStd),  readingMean + (3* readingStd)

    R_counterStd1 = 0
    R_counterStd2 = 0
    R_counterStd3 = 0

    for i in range(0, len(readingScore)):
        value = readingScore[i]
        if value >= sd1_Start and value <= sd1_End:
            R_counterStd1 += 1

        if value >= sd2_Start and value <= sd2_End:
            R_counterStd2 += 1

        if value >= sd3_Start and value <= sd3_End:
            R_counterStd3 += 1

    R_perOfSd1 = (R_counterStd1*100)/len(readingScore)
    R_perOfSd2 = (R_counterStd2*100)/len(readingScore)
    R_perOfSd3 = (R_counterStd3*100)/len(readingScore)

    print('\n Reading Std1: ',R_perOfSd1)
    print(' Reading Std2: ',R_perOfSd2)
    print(' Reading Std3: ',R_perOfSd3)




    # Writing Score

    sd1_Start, sd1_End = writingMean - writingStd, writingMean + writingStd
    sd2_Start, sd2_End =  writingMean - (2* writingStd),  writingMean + (2* writingStd)
    sd3_Start, sd3_End =  writingMean - (3* writingStd),  writingMean + (3* writingStd)

    W_counterStd1 = 0
    W_counterStd2 = 0
    W_counterStd3 = 0

    for i in range(0, len(readingScore)):
        value = readingScore[i]
        if value >= sd1_Start and value <= sd1_End:
            W_counterStd1 += 1

        if value >= sd2_Start and value <= sd2_End:
            W_counterStd2 += 1

        if value >= sd3_Start and value <= sd3_End:
            W_counterStd3 += 1

    W_perOfSd1 = (W_counterStd1*100)/len(readingScore)
    W_perOfSd2 = (W_counterStd2*100)/len(readingScore)
    W_perOfSd3 = (W_counterStd3*100)/len(readingScore)

    print('\n Writing Std1: ',W_perOfSd1)
    print(' Writing Std2: ',W_perOfSd2)
    print(' Writing Std3: ',W_perOfSd3)



Mean_Median_Mode()

input("\n\nPlease Press Enter to Load the Graph")

graph1 = ff.create_distplot([mathsScore, readingScore, writingScore], [
                            'Maths Score', 'ReadingScore', 'WritingScore'], show_hist=False)
graph1.show()
