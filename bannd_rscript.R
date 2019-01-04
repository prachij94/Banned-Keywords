df1 <- read.csv("C:/Users/Imart/Downloads/rejected.csv",sep = "\n")
df2 <- read.csv("C:/Users/Imart/Downloads/rejected.csv",sep = ",",header = F)


df_approved_pr <- read.table("C:/Users/Imart/Downloads/approved.csv",sep = ",",blank.lines.skip = TRUE,fill = T)
?read.csv

df_appr_bl <- readxl::read_excel("C:/Users/Imart/Downloads/BL approved (1).xlsx",sheet = 1)

df_rej_bl1 <- readxl::read_excel("C:/Users/Imart/Downloads/Buylead_oct'17-sep'18.xlsx",sheet = 1)

df_rej_bl2 <- readxl::read_excel("C:/Users/Imart/Downloads/buylead_2016-2017.xlsx",sheet = 1)

df_rej_bl3 <- readxl::read_excel("C:/Users/Imart/Downloads/buylead_15-16.xlsx",sheet = 1)

colnames(df_rej_bl1)
colnames(df_rej_bl2)
colnames(df_rej_bl3)

bl_3yrs_rej <- rbind(df_rej_bl1,df_rej_bl2,df_rej_bl3)

write.csv(bl_3yrs_rej,"BL_3yrs_reject.csv",row.names = F,quote = F)

## Reading file updated one

#Banned <- read.csv("E:/Banned_KW/3yearssuspected/testrej.csv",blank.lines.skip = F,sep = "\t",header = F)

df_app_pr <- readxl::read_excel("E:/BANNED/ApprovedDataLabels1.xlsx",sheet = 1)

df_rej_pr <- readxl::read_excel("E:/BANNED/RejectDataLabels.xlsx",sheet = 1)

df_app_pr$Test <- paste0(df_app_pr$Item_Name," ",df_app_pr$Description1)
df_app_pr$Label <- paste0("__label__Approved ",df_app_pr$Test)

colnames(df_app_pr)[4] <- "Keyword"
colnames(df_rej_pr)[4] <- "Keyword"

df_rej_pr$Test <- paste0(df_rej_pr$Item_Name," ",df_rej_pr$Description1)
df_rej_pr$Label <- paste0("__label__Rejected ",df_rej_pr$Test)


setwd('E:/BANNED/')

getwd()

df_app_pr$Status <- "Approved"

df_rej_pr$Status <- "Rejected"


Rejected_data <- rbind(df_rej_pr,df_rej_pr)

Final_data <- rbind(df_app_pr,Rejected_data)


final_df <- Final_data[sample(nrow(Final_data)),]


TrainIndex <- seq(1:floor(nrow(final_df)*.90))

Train_data <- final_df[TrainIndex,]
Test_data <- final_df[-TrainIndex,]


write.csv(final_df,"Compiled_data.csv",row.names = F,quote = F)
write.csv(Test_data,"Testing_vlookup.csv",row.names = F,quote = F)

write.table(Train_data$Label,"train.txt",row.names = F,col.names = F,quote = F)
write.table(Test_data$Test,"test.txt",row.names = F,col.names = F,quote = F)











