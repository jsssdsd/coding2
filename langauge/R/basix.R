sugar <- 25
water <- 125
percent <- sugar / (sugar + water) * 100
print(percent)

a <- 7
b <- 9
c <- a*b
print(c)

a <- 90
b <- 60
c <- 80
d <- (360-a+b+c)/4
print(d)

a <- 4
b <- 3
c <- a*b/2
print(c)

#속력 = 거리 /시간

v1 <- 20
v2 <- 30
v3 <- v1/20 + v2 / 30

print(v3)

v <- c(92,43,55,28,19)
print(v)

v1 <- c('cyan','magenta','yellow','black')
print(v1)

v <- c(1,2,3,4)
sum(v)

v1 <- c('T','T','T','F','T','F','F','T','T','F')
sum(v1)

V2 <- C(T,T,T,F,T,F,F,T,T,F)

sum(V2)

v1 <- 1:5000
sum(v1)


even <- seq(0,100,2)
print(even)

d <- 1:100
print(d)

odd <- d[seq(1,100,2)]
odd <- d[seq(1,length(d),2)]
print(odd)
le <- length(odd) -10
odd[-c(le:length(odd))]
pick <- odd[c(3,7,32)]
pick

names(pick) <- c('3rd','7th','32th')
pick


d <- c(1,4,3,7,8)
2*d
d-5
3*d + 4

v <- c(6,1,3,7,9)
2*v - 1
print(v)

x <- c(1,2,3,4)
y <- c(5,6,7,8)
x+y
x*y
z <- x + y
z
0
v1 <- c(1,2,3,4)
v2 <- c('John','Jane','Tom')
v3 <- c(v1,v2)
v3

a <- c(3,6,9,12,15)
b <- c(18,21,24,27,30)
c <- c(-1,2,-2,5,-7)
d <- c('1',1,1,1,1)

x <- c(a,b)
y <- c(d,c)

a + 3 *c
x+y


d <- c(1,2,3,4,5,6,7,8,9,10)
sum(d)
sum(2*d)
length(d)
mean(d[1:5])
max(d)
min(d)
sort(d)
sort(d, decreasing = FALSE)
sort(d, decreasing = TRUE)
v1 <- median(d)
v1
v2 <-sum(d)/length(d)


a <- seq(from = 20, to = 80, by = 7)
length(a)
sort(a,decreasing = T)
max(a)
min(a)
range(a)
mean(a)
median(a)
var(a)
sd(a)










