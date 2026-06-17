![](data:image/png;base64...)

Lab Assignment-01

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Only for Course Teacher** | | | | | | |
|  | | **Needs Improvement** | **Developing** | **Sufficient** | **Above Average** | **Total Mark** |
| **Allocate mark & Percentage** | | **25%** | **50%** | **75%** | **100%** | **15** |
| **Problem Analysis** | **03** |  |  |  |  |  |
| **Solution Design** | **02** |  |  |  |  |  |
| **Code Development** | **06** |  |  |  |  |  |
| **Accuracy** | **04** |  |  |  |  |  |
| **Total obtained mark** | | | | | |  |
| **Comments** |  | | | | | |

**Semester: Spring 2025**

**Student Name: Tanjina Alam Tisha**

**Student ID:252-35-585**

**Batch:** 45

**Section: E-2**

**Course Code:** SE 133

**Course Name:** Software Development Capstone Project

**Course Teacher Name:** Jafrin Iqbal Chowdhury

**Designation:** Lecturer

**Submission Date: 07.06.2026**

**Sheet 1**

A.

![](data:image/png;base64...)

B.

![](data:image/png;base64...)

C.

![](data:image/png;base64...)

D.

![](data:image/png;base64...)

E.

![](data:image/png;base64...)

F.

![](data:image/png;base64...)

H.

![](data:image/png;base64...)

U.

![](data:image/png;base64...)

I.

![](data:image/png;base64...)

K.

![](data:image/png;base64...)

J.

![](data:image/png;base64...)

M.

![](data:image/png;base64...)

V.

![](data:image/png;base64...)

W.

![](data:image/png;base64...)

X.

![](data:image/png;base64...)

Y.

![](data:image/png;base64...)

Z.

![](data:image/png;base64...)

**Sheet 2**

**A.**

![](data:image/png;base64...)

B.

![](data:image/png;base64...)

C.

![](data:image/png;base64...)

D.

![](data:image/png;base64...)

E.

![](data:image/png;base64...)

F.

![](data:image/png;base64...)

G.

![](data:image/png;base64...)

H.

![](data:image/png;base64...)

I.

![](data:image/png;base64...)

J.

![](data:image/png;base64...)

K.

![](data:image/png;base64...)

L.

![](data:image/png;base64...)

M.

![](data:image/png;base64...)

N.

![](data:image/png;base64...)

**Uva/ Online Judge Code**

**10071 - Back to High School Physics**

Code:

#include <stdio.h> int main() {

int v, t, s;

while(scanf("%d%d", &v, &t)!=EOF) {

s = (2*v*t);

printf("%d\n", s); }

return 0;

}

Ss:

![](data:image/png;base64...)

**10035 - Primary Arithmetic**

**Code:**

#include <stdio.h>

int main()

{

unsigned long long a, b;

int sum1 = 0, d1, d2;

while(scanf("%llu%llu", &a, &b) == 2)

{

if (a == 0 && b == 0)

{

break;

}

int c\_c = 0;

int c = 0;

while(a > 0 || b > 0)

{

d1 = a % 10;

d2 = b % 10;

sum1 = d1 + d2 + c;

if (sum1 > 9)

{

c = 1;

c\_c++;

}

else

{

c = 0;

}

a /= 10;

b /= 10;

}

if (c\_c == 0)

{

printf("No carry operation.\n");

}

else if (c\_c == 1)

{

printf("1 carry operation.\n");

}

else

{

printf("%d carry operations.\n", c\_c);

}

}

return 0;

}

SS:

![](data:image/png;base64...)

**10055 - Hashmat the Brave Warrior**

Code:

#include <stdio.h>

int main()
{
 long long a, b, c;
 while(scanf("%lld%lld", &a, &b) != EOF)
 {
 c = b - a;
 if (c < 0)
 {
 c = (c \* (-1));
 }
 printf("%lld\n", c);
 }
 return 0;
}

Ss:

![](data:image/png;base64...)

**10235 - Simply Emirp**

Code:

#include <stdio.h>

int main()
{
 long long n, m, i;

 while(scanf("%lld", &n) != EOF)
 {
 if (n <= 1)
 {
 printf("%lld is not prime.\n", n);
 continue;
 }

 m = 1;
 for (i = 2; i \* i <= n; i++)
 {
 m = n % i;
 if (m == 0)
 {
 break;
 }
 }

 if (m == 0)
 {
 printf("%lld is not prime.\n", n);
 }
 else
 {
 long long temp = n;
 long long reversed = 0;
 while (temp > 0)
 {
 int rem = temp % 10;
 reversed = (reversed \* 10) + rem;
 temp /= 10;
 }

 if (reversed == n)
 {
 printf("%lld is prime.\n", n);
 }
 else
 {
 long long rev\_m = 1;
 for (i = 2; i \* i <= reversed; i++)
 {
 if (reversed % i == 0)
 {
 rev\_m = 0;
 break;
 }
 }

 if (rev\_m != 0)
 {
 printf("%lld is emirp.\n", n);
 }
 else
 {
 printf("%lld is prime.\n", n);
 }
 }
 }
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**11854 - Egypt**

Code:

#include <stdio.h>
#include <math.h>

int main()
{
 long long a, b, c, sqA, sqB, sqC;
 while(scanf("%lld%lld%lld", &a, &b, &c) == 3)
 {
 if(a == 0 && b == 0 && c == 0)
 {
 break;
 }
 sqA = a \* a;
 sqB = b \* b;
 sqC = c \* c;
 if ( (sqA + sqB == sqC) || (sqA == sqB + sqC) || (sqA + sqC == sqB) )
 {
 printf("right\n");
 }
 else
 {
 printf("wrong\n");
 }
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**11727 - Cost Cutting**

Code:

#include <stdio.h>

int main()
{
 int t, s1, s2, s3, i, mid;
 scanf("%d", &t);

 for(i = 1; i <= t; i++)
 {
 scanf("%d%d%d", &s1, &s2, &s3);
 if ((s1 > s2 && s1 > s3 && s3 < s1 && s3 < s2) || (s1 < s2 && s1 < s3 && s3 > s1 && s3 > s2))
 {
 mid = s2;
 }
 else if ((s2 > s1 && s2 > s3 && s3 < s1 && s3 < s2) || (s2 < s1 && s2 < s3 && s3 > s1 && s3 > s2))
 {
 mid = s1;
 }
 else
 {
 mid = s3;
 }
 printf("Case %d: %d\n", i, mid);
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**12403 - Save Setu**

Code:

#include <stdio.h>
#include <string.h>

int main()
{
 long long t, amount, total\_amount = 0;
 int i;
 char cmd[50];
 scanf("%lld", &t);
 for (i = 1; i <= t; i++)
 {
 scanf("%s", cmd);
 if (strcmp(cmd, "donate") == 0)
 {
 scanf("%lld", &amount);
 total\_amount += amount;
 }
 else if (strcmp(cmd, "report") == 0)
 {
 printf("%lld\n", total\_amount);
 }
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**10070 - Leap Year or Not Leap Year and ...**

Code:

#include <stdio.h>
#include <string.h>

#define MAX\_DIGITS 10005

int is\_divisible(const char \*year, int divisor) {
 int remainder = 0;
 for (int i = 0; year[i] != '\0'; i++) {
 remainder = (remainder \* 10 + (year[i] - '0')) % divisor;
 }
 return remainder == 0;
}

int main() {
 char year[MAX\_DIGITS];
 int first\_output = 1;

 while (scanf("%s", year) == 1) {
 if (!first\_output) {
 printf("\n");
 }
 first\_output = 0;

 int is\_leap = 0;
 int is\_hulu = 0;
 int is\_bulu = 0;
 int is\_ordinary = 1;

 if (is\_divisible(year, 400) || (is\_divisible(year, 4) && !is\_divisible(year, 100))) {
 is\_leap = 1;
 is\_ordinary = 0;
 }

 if (is\_divisible(year, 15)) {
 is\_hulu = 1;
 is\_ordinary = 0;
 }

 if (is\_leap && is\_divisible(year, 55)) {
 is\_bulu = 1;
 is\_ordinary = 0;
 }

 if (is\_leap) {
 printf("This is leap year.\n");
 }
 if (is\_hulu) {
 printf("This is huluculu festival year.\n");
 }
 if (is\_bulu) {
 printf("This is bulukulu festival year.\n");
 }
 if (is\_ordinary) {
 printf("This is an ordinary year.\n");
 }
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**12289 - One-Two-Three**

Code:

#include <stdio.h>
#include <string.h>

int main()
{
 int n, i;
 char x[12];
 scanf("%d", &n);
 for (i = 1; i <= n; i++)
 {
 scanf("%s", x);
 if (strlen(x) == 5)
 {
 printf("3\n");
 }
 else if (strlen(x) == 3)
 {
 int match\_count = 0;
 if (x[0] == 'o')
 {
 match\_count++;
 }
 if (x[1] == 'n')
 {
 match\_count++;
 }
 if (x[2] == 'e')
 {
 match\_count++;
 }
 if (match\_count >= 2)
 {
 printf("1\n");
 }
 else
 {
 printf("2\n");
 }
 }
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**11547 - Automatic Answer**

Code:

#include <stdio.h>
#include <stdlib.h>

int main()
{
 int t, n, i;
 scanf("%d", &t);
 for (i = 0; i < t; i++)
 {
 scanf("%d", &n);
 int ans = ((((((n \* 567) / 9) + 7492) \* 235) / 47) - 498);
 int rem = ans % 100;
 int f\_ans = rem / 10;
 printf("%d\n", abs(f\_ans));
 }
 return 0;
}

SS:

![](data:image/png;base64...)

**10696 - f91**

Code:

#include <stdio.h>

int main()
{
 long long n;
 while (scanf("%lld", &n) == 1 && n != 0)
 {
 if (n >= 101)
 {
 printf("f91(%lld) = %lld\n", n, n - 10);
 }
 else if (n <= 100)
 {
 printf("f91(%lld) = 91\n", n);
 }
 }
 return 0;
}

SS:

![](data:image/png;base64...)

### **100 - The 3n + 1 problem**

Code:

#include <stdio.h>

int main() {

int i, j;

while( scanf("%d%d", &i,&j) !=EOF){

int oi=i;

int oj=j;

if (i>j){

int ts=i;

i=j;

j=ts;

}

int maxL=0;

for(int n=i;n<=j;n++){

long long temp=n;

int cc=1;

while (temp>1){

if(temp%2==0){

temp=temp/2;}

else {

temp=(3\*temp)+1;

}

cc++;

}

if(cc>maxL){

maxL=cc;

}

}

printf("%d %d %d\n",oi,oj,maxL);

}

return 0;

}

Ss:![](data:image/png;base64...)

**10050 - Hartals**

Code:

#include <stdio.h>

int main() {
 int t;
 if (scanf("%d", &t) != 1) return 0;

 while (t--) {
 int n, p;
 int h[105];
 int i, j;
 int lost\_days = 0;

 if (scanf("%d", &n) != 1) break;
 if (scanf("%d", &p) != 1) break;

 for (i = 0; i < p; i++) {
 scanf("%d", &h[i]);
 }

 for (i = 1; i <= n; i++) {
 if (i % 7 == 6 || i % 7 == 0) {
 continue;
 }

 int hartal\_today = 0;
 for (j = 0; j < p; j++) {
 if (i % h[j] == 0) {
 hartal\_today = 1;
 break;
 }
 }

 if (hartal\_today) {
 lost\_days++;
 }
 }

 printf("%d\n", lost\_days);
 }

 return 0;
}

SS:

![](data:image/png;base64...)

**11332 - Summing Digits**

Code:

#include <stdio.h>

long long get\_digit\_sum(long long n) {
 long long sum = 0;
 while (n > 0) {
 sum += n % 10;
 n /= 10;
 }
 return sum;
}

int main() {
 long long n;

 while (scanf("%lld", &n) == 1 && n != 0) {
 while (n >= 10) {
 n = get\_digit\_sum(n);
 }
 printf("%lld\n", n);
 }

SS:

![](data:image/png;base64...)

**11498 - Division of Nlogonia**

c

#include <stdio.h>

int main() {
 int k;

 while (scanf("%d", &k) == 1 && k != 0) {
 int n, m;
 int i;
 scanf("%d %d", &n, &m);

 for (i = 0; i < k; i++) {
 int x, y;
 scanf("%d %d", &x, &y);

 if (x == n || y == m) {
 printf("divisa\n");
 } else if (x > n && y > m) {
 printf("NE\n");
 } else if (x < n && y > m) {
 printf("NO\n");
 } else if (x < n && y < m) {
 printf("SO\n");
 } else if (x > n && y < m) {
 printf("SE\n");
 }
 }
 }

 return 0;
}

SS:

![](data:image/png;base64...)