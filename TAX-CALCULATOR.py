{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 income = float(input("Enter the annual income: "))\
if (10000<= income <= 85528):\
    Tax = ((income*18)/100)-556.2\
elif income >= 85528: \
    Tax =((income- 85528)*32)/100+14839.2\
elif (-100 <= income<=1000): \
    Tax = 0.0\
Tax = round(Tax, 0)\
print("The tax is:", Tax, "thalers")}