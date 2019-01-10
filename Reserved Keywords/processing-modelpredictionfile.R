# processing final data:
options(scipen = 999)
#options("scipen"=100, "digits"=4)
#format(1810032000, scientific = FALSE)
library(psych)
library("readxl")
library("xlsx")
library("stringr")
library("stringi")
library("dplyr")
library("stopwords")
library("tm")
library("qdapRegex")


Files <- list.files(path = "c:/Users/prachi/Downloads/Ban Logs/final/",pattern = ".csv$")


m <- 5

for (m in 6:7) {
  
  locations <- paste0("c:/Users/prachi/Downloads/Ban Logs/final/",Files[m])
  df <- read.csv(locations,header = F,sep = ",",fill = T)
  
  
  #df <- read.csv("C:/Users/prachi/Downloads/Ban Logs/final/final_result.csv",header = F,sep = ",",fill = T)
  colnames(df)[1] <- "V1"
  df <- data.frame(df[,"V1"])
  sum(df$V1=="")
  #df$df....V1.. <- as.character(df$df....V1..)   
  #  for (j in nrow(df)) {
  #   ifelse(nchar(df$df....V1..[j])>200,df$df....V1..[j] <- paste(word(df$df....V1..[j],1),word(df$df....V1..[j],2),word(df$df....V1..[j],3),word(df$df....V1..[j],4)),df$df....V1..[j] <- as.character(df$df....V1..[j]))
  #}
  
  Index <- seq(1,nrow(df),2)
  Index2 <- seq(2,nrow(df),2)
  df_check <- data.frame(df[Index,])
  df_check2 <- data.frame(df[Index2,])
  which(grepl("__label__",df_check)==T)
  sum(grepl("__label__",df_check2))
  
  class(paste(word(df$df....V1..[1],1),word(df$df....V1..[1],2),word(df$df....V1..[1],3),word(df$df....V1..[1],4)))
  length <- nrow(df)
  #Creating two empty dataframes
  my_df<-data.frame(df.i...=character()) 
  my_df1<-data.frame(df.i...=character())
  #df<-df[-c(10060,13358),]
  #df<-data.frame(df)
  #for(i in seq(from=1,to=length,by=2)){
  
  # a<-data.frame(df[i,])
  #b<-data.frame(df[i+1,])
  #my_df<-rbind(my_df,a)
  #my_df1<-rbind(my_df1,b)
  #}
  
  
  #sum(grepl("__label__",a$df.i...))
  #sum(grepl("__label__",b$df.i...1...))
  
  #my_df$df.i... <- as.character(my_df$df.i...)
  #my_df1$df.i...1... <- as.character(my_df1$df.i...1...)
  # Creating a dataframe new_df by joining two dataframe my_df and my_df1
  #new_df<-cbind(my_df,my_df1)
  
  new_df <- cbind(df_check,df_check2)
  colnames(new_df)
  #new_df <- new_df[-nrow(new_df),]
  # renaming columns
  new_df<-rename(new_df,V1=df.Index...)
  new_df<-rename(new_df,V2=df.Index2...)
  #new_df<-data.frame(paste0(new_df$V1," ",new_df$V2))
  #new_df<-rename(new_df,V1=paste0.new_df.V1.......new_df.V2.)
  
  #colnames(new_df)[names(new_df)=="df.i..."] <- V1
  
  
  #splitting word data:
  # removing last comma character from column
  char_array <-new_df$V2
  a <-data.frame("data"=char_array,"data2"=1)
  a$data<-as.character(a$data)
  new_df$V2 = substr(a$data,1,nchar(a$data)-1)
  
  #Extracting probability based on whitespace as delimiter
  new_df$probability2<-word(new_df$V2,-1)
  
  # Extracting label
  new_df$labelname1<-word(new_df$V2,-4)
  new_df$labelname1 <- gsub("__label__","",new_df$labelname1)
  new_df$labelname1 <- gsub("_"," ",new_df$labelname1)
  
  # Extracting second labelname_match
  new_df$labelname2<-word(new_df$V2,-2)
  # Replacing __label__ with empty
  new_df$labelname2<-gsub("__label__", "", new_df$labelname2)
  new_df$labelname2 <- gsub("_"," ",new_df$labelname2)
  #new_df$third<-gsub("_", " ", new_df$third)
  new_df$probability1 <- word(new_df$V2,-3)
  
  final_out <- new_df[,c(1,2,4,6,5,3)]
  final_out <- rename(final_out,test_data=V1)
  final_out[2,]
  index <- grepl("e",final_out$probability2)
  #index <- as.character(index)
  for (i in 1:nrow(final_out)) {
    ifelse(index[i]==TRUE,final_out$probability2[i] <- 0,final_out$probability2[i] <- as.numeric(final_out$probability2[i]))
  }
  
  #final_out$probability2 <- format(final_out$probability2,scientific = FALSE)
  for (k in 1:nrow(final_out)) {
    ifelse(final_out$labelname1[k]=="",final_out$labelname1[k] <- as.character(final_out$labelname2[k]),final_out$labelname1[k] <- final_out$labelname1[k])
  }
  
  for (k in 1:nrow(final_out)) {
    ifelse(final_out$probability1[k]=="",final_out$probability1[k] <- as.numeric(final_out$probability2[k]),final_out$probability1[k] <- final_out$probability1[k])
  }
  
  Index3 <- (final_out$labelname1==final_out$labelname2)
  for (k in 1:nrow(final_out)) {
    ifelse(Index3[k]==TRUE,final_out$labelname2[k] <- "",final_out$labelname2[k] <- final_out$labelname2[k] )
  }
  
  for (k in 1:nrow(final_out)) {
    ifelse(Index3[k]==TRUE,final_out$probability2[k] <- "",final_out$probability2[k] <- final_out$probability2[k] )
  }
  #options(digits = 22)
  #library(bit64)
  #inal_out$probability2 <- as.integer64(final_out$probability2)
  #as.integer()
  #write_csv(tbl_df,'test.csv')
  location2 <- paste0("c:/Users/prachi/Downloads/Ban Logs/final/K",Files[m])
  write.csv(final_out,location2,row.names = F,quote = F)
  #write.csv(final_out,"C:/Users/prachi/Downloads/Ban Logs/final/final_processed_data3.csv",row.names = F,quote = F)
  
}

