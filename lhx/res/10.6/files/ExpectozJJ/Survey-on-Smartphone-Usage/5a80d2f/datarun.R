survey = read.csv('D:/OneDrive for Business/Lecture Notes Y3S2/HW0228/PSQI.csv')

PSQIGlobal = survey$PSQIGlobal
PSQIDURAT = survey$PSQIDURAT
PSQIDISTB = survey$PSQIDISTB
PSQILATEN = survey$PSQILATEN
PSQIDAYSDYS = survey$PSQIDAYSDYS
PSQIHSE = survey$PSQIHSE
PSQISLPQUAL = survey$PSQISLPQUAL
PSQIMEDS = survey$PSQIMEDS


gender = survey$Gender

div = survey$Division

weight = survey$Weight

height = survey$Height

bmi = weight/(height^2)

bed = survey$Smartphone.in.Bed

usage = survey$Smartphone.Usage

activity = rep(0,nrow(survey)) 

activity[survey$Social.Media == 1] = 'Social Media'

activity[survey$Videos == 1] = 'Videos'

activity[survey$Gaming == 1] = 'Gaming'

activity[survey$Internet == 1] = 'Internet'

activity[survey$Instant.Messaging == 1] = 'Instant Messaging'

activity[survey$Online.Shopping == 1] = 'Online Shopping'

survey = data.frame(gender, div, bmi, PSQIDURAT, PSQIDISTB, PSQILATEN,PSQIDAYSDYS, PSQIHSE, PSQISLPQUAL, PSQIMEDS, PSQIGlobal, usage, bed, activity)

survey.nonsu = survey[survey$bed == 'No',]
survey.su = survey[survey$bed == 'Yes',] 

model1 = lm(PSQIGlobal ~ usage + gender, data = survey.su)

model2 = lm(PSQIGlobal ~ usage + div, data = survey.su)

model3 = lm(PSQIGlobal ~ usage + activity, data = survey.su)

model4 = lm(PSQIGlobal ~ usage + bmi, data = survey.su)

model5 = lm(PSQIGlobal ~ usage, data = survey.su)

summary(model5)

anova(model4)

anova(model3)

anova(model2)

anova(model1)

