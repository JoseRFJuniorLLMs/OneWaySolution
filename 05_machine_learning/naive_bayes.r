library(e1071)

caixa = read.csv('dataset.csv',sep=';',header=T)
caixa <- caixa[c('Vara',
'Foro',
'Comarca',
'Advogado',
'Centro.de.Custo',
'Unidade.Subsidio',
'Vr..Causa',
'Vr..Causa.Atual',
'iCodDocumento',
'Grupo.de.Assunto',
'Acao')]

caixa$Acao <- as.factor(caixa$Acao)
amostra = sample(2,nrow(caixa),replace=T, prob=c(0.8,0.3))
caixatreino = caixa[amostra==1,]
caixateste = caixa[amostra==2,]

modelo <- naiveBayes(Acao ~., caixatreino)
predicao <- predict(modelo,caixateste)
confusao = table(caixateste$Acao,predicao)
table(caixateste$Acao,predicao)

sum(diag(confusao))/nrow(caixa)