# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Balancesheetnonfin(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    c4 = models.FloatField(db_column='C4', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7', blank=True, null=True)  # Field name made lowercase.
    c8 = models.FloatField(db_column='C8', blank=True, null=True)  # Field name made lowercase.
    c9 = models.FloatField(db_column='C9', blank=True, null=True)  # Field name made lowercase.
    c10 = models.FloatField(db_column='C10', blank=True, null=True)  # Field name made lowercase.
    c11 = models.FloatField(db_column='C11', blank=True, null=True)  # Field name made lowercase.
    c12 = models.FloatField(db_column='C12', blank=True, null=True)  # Field name made lowercase.
    c13 = models.FloatField(db_column='C13', blank=True, null=True)  # Field name made lowercase.
    c14 = models.FloatField(db_column='C14', blank=True, null=True)  # Field name made lowercase.
    c15 = models.FloatField(db_column='C15', blank=True, null=True)  # Field name made lowercase.
    c16 = models.FloatField(db_column='C16', blank=True, null=True)  # Field name made lowercase.
    c17 = models.FloatField(db_column='C17', blank=True, null=True)  # Field name made lowercase.
    c18 = models.FloatField(db_column='C18', blank=True, null=True)  # Field name made lowercase.
    c19 = models.FloatField(db_column='C19', blank=True, null=True)  # Field name made lowercase.
    c20 = models.FloatField(db_column='C20', blank=True, null=True)  # Field name made lowercase.
    c21 = models.FloatField(db_column='C21', blank=True, null=True)  # Field name made lowercase.
    c22 = models.FloatField(db_column='C22', blank=True, null=True)  # Field name made lowercase.
    c23 = models.FloatField(db_column='C23', blank=True, null=True)  # Field name made lowercase.
    c24 = models.FloatField(db_column='C24', blank=True, null=True)  # Field name made lowercase.
    c25 = models.FloatField(db_column='C25', blank=True, null=True)  # Field name made lowercase.
    c26 = models.FloatField(db_column='C26', blank=True, null=True)  # Field name made lowercase.
    c27 = models.FloatField(db_column='C27', blank=True, null=True)  # Field name made lowercase.
    c28 = models.FloatField(db_column='C28', blank=True, null=True)  # Field name made lowercase.
    c29 = models.FloatField(db_column='C29', blank=True, null=True)  # Field name made lowercase.
    c30 = models.FloatField(db_column='C30', blank=True, null=True)  # Field name made lowercase.
    c31 = models.FloatField(db_column='C31', blank=True, null=True)  # Field name made lowercase.
    c32 = models.FloatField(db_column='C32', blank=True, null=True)  # Field name made lowercase.
    c33 = models.FloatField(db_column='C33', blank=True, null=True)  # Field name made lowercase.
    c34 = models.FloatField(db_column='C34', blank=True, null=True)  # Field name made lowercase.
    c35 = models.FloatField(db_column='C35', blank=True, null=True)  # Field name made lowercase.
    c36 = models.FloatField(db_column='C36', blank=True, null=True)  # Field name made lowercase.
    c37 = models.FloatField(db_column='C37', blank=True, null=True)  # Field name made lowercase.
    c38 = models.FloatField(db_column='C38', blank=True, null=True)  # Field name made lowercase.
    c39 = models.FloatField(db_column='C39', blank=True, null=True)  # Field name made lowercase.
    c40 = models.FloatField(db_column='C40', blank=True, null=True)  # Field name made lowercase.
    c41 = models.FloatField(db_column='C41', blank=True, null=True)  # Field name made lowercase.
    c42 = models.FloatField(db_column='C42', blank=True, null=True)  # Field name made lowercase.
    c43 = models.FloatField(db_column='C43', blank=True, null=True)  # Field name made lowercase.
    c44 = models.FloatField(db_column='C44', blank=True, null=True)  # Field name made lowercase.
    c45 = models.FloatField(db_column='C45', blank=True, null=True)  # Field name made lowercase.
    c46 = models.FloatField(db_column='C46', blank=True, null=True)  # Field name made lowercase.
    c47 = models.FloatField(db_column='C47', blank=True, null=True)  # Field name made lowercase.
    c48 = models.FloatField(db_column='C48', blank=True, null=True)  # Field name made lowercase.
    c49 = models.FloatField(db_column='C49', blank=True, null=True)  # Field name made lowercase.
    c50 = models.FloatField(db_column='C50', blank=True, null=True)  # Field name made lowercase.
    c51 = models.FloatField(db_column='C51', blank=True, null=True)  # Field name made lowercase.
    c52 = models.FloatField(db_column='C52', blank=True, null=True)  # Field name made lowercase.
    c53 = models.FloatField(db_column='C53', blank=True, null=True)  # Field name made lowercase.
    c54 = models.FloatField(db_column='C54', blank=True, null=True)  # Field name made lowercase.
    c55 = models.FloatField(db_column='C55', blank=True, null=True)  # Field name made lowercase.
    c56 = models.FloatField(db_column='C56', blank=True, null=True)  # Field name made lowercase.
    c57 = models.FloatField(db_column='C57', blank=True, null=True)  # Field name made lowercase.
    c58 = models.FloatField(db_column='C58', blank=True, null=True)  # Field name made lowercase.
    c59 = models.FloatField(db_column='C59', blank=True, null=True)  # Field name made lowercase.
    c60 = models.FloatField(db_column='C60', blank=True, null=True)  # Field name made lowercase.
    c61 = models.FloatField(db_column='C61', blank=True, null=True)  # Field name made lowercase.
    c62 = models.FloatField(db_column='C62', blank=True, null=True)  # Field name made lowercase.
    c63 = models.FloatField(db_column='C63', blank=True, null=True)  # Field name made lowercase.
    c64 = models.FloatField(db_column='C64', blank=True, null=True)  # Field name made lowercase.
    c65 = models.FloatField(db_column='C65', blank=True, null=True)  # Field name made lowercase.
    c66 = models.FloatField(db_column='C66', blank=True, null=True)  # Field name made lowercase.
    c67 = models.FloatField(db_column='C67', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BalanceSheetNonFin'


class Cashflownonfin(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    c4 = models.FloatField(db_column='C4', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7', blank=True, null=True)  # Field name made lowercase.
    c8 = models.FloatField(db_column='C8', blank=True, null=True)  # Field name made lowercase.
    c9 = models.FloatField(db_column='C9', blank=True, null=True)  # Field name made lowercase.
    c10 = models.FloatField(db_column='C10', blank=True, null=True)  # Field name made lowercase.
    c11 = models.FloatField(db_column='C11', blank=True, null=True)  # Field name made lowercase.
    c12 = models.FloatField(db_column='C12', blank=True, null=True)  # Field name made lowercase.
    c13 = models.FloatField(db_column='C13', blank=True, null=True)  # Field name made lowercase.
    c14 = models.FloatField(db_column='C14', blank=True, null=True)  # Field name made lowercase.
    c15 = models.FloatField(db_column='C15', blank=True, null=True)  # Field name made lowercase.
    c16 = models.FloatField(db_column='C16', blank=True, null=True)  # Field name made lowercase.
    c17 = models.FloatField(db_column='C17', blank=True, null=True)  # Field name made lowercase.
    c18 = models.FloatField(db_column='C18', blank=True, null=True)  # Field name made lowercase.
    c19 = models.FloatField(db_column='C19', blank=True, null=True)  # Field name made lowercase.
    c20 = models.FloatField(db_column='C20', blank=True, null=True)  # Field name made lowercase.
    c21 = models.FloatField(db_column='C21', blank=True, null=True)  # Field name made lowercase.
    c22 = models.FloatField(db_column='C22', blank=True, null=True)  # Field name made lowercase.
    c23 = models.FloatField(db_column='C23', blank=True, null=True)  # Field name made lowercase.
    c24 = models.FloatField(db_column='C24', blank=True, null=True)  # Field name made lowercase.
    c25 = models.FloatField(db_column='C25', blank=True, null=True)  # Field name made lowercase.
    c26 = models.FloatField(db_column='C26', blank=True, null=True)  # Field name made lowercase.
    c27 = models.FloatField(db_column='C27', blank=True, null=True)  # Field name made lowercase.
    c28 = models.FloatField(db_column='C28', blank=True, null=True)  # Field name made lowercase.
    c29 = models.FloatField(db_column='C29', blank=True, null=True)  # Field name made lowercase.
    c30 = models.FloatField(db_column='C30', blank=True, null=True)  # Field name made lowercase.
    c31 = models.FloatField(db_column='C31', blank=True, null=True)  # Field name made lowercase.
    c32 = models.FloatField(db_column='C32', blank=True, null=True)  # Field name made lowercase.
    c33 = models.FloatField(db_column='C33', blank=True, null=True)  # Field name made lowercase.
    c34 = models.FloatField(db_column='C34', blank=True, null=True)  # Field name made lowercase.
    c35 = models.FloatField(db_column='C35', blank=True, null=True)  # Field name made lowercase.
    c36 = models.FloatField(db_column='C36', blank=True, null=True)  # Field name made lowercase.
    c37 = models.FloatField(db_column='C37', blank=True, null=True)  # Field name made lowercase.
    c38 = models.FloatField(db_column='C38', blank=True, null=True)  # Field name made lowercase.
    c39 = models.FloatField(db_column='C39', blank=True, null=True)  # Field name made lowercase.
    c40 = models.FloatField(db_column='C40', blank=True, null=True)  # Field name made lowercase.
    c41 = models.FloatField(db_column='C41', blank=True, null=True)  # Field name made lowercase.
    c42 = models.FloatField(db_column='C42', blank=True, null=True)  # Field name made lowercase.
    c43 = models.FloatField(db_column='C43', blank=True, null=True)  # Field name made lowercase.
    c44 = models.FloatField(db_column='C44', blank=True, null=True)  # Field name made lowercase.
    c45 = models.FloatField(db_column='C45', blank=True, null=True)  # Field name made lowercase.
    c46 = models.FloatField(db_column='C46', blank=True, null=True)  # Field name made lowercase.
    c47 = models.FloatField(db_column='C47', blank=True, null=True)  # Field name made lowercase.
    c48 = models.FloatField(db_column='C48', blank=True, null=True)  # Field name made lowercase.
    c49 = models.FloatField(db_column='C49', blank=True, null=True)  # Field name made lowercase.
    c50 = models.FloatField(db_column='C50', blank=True, null=True)  # Field name made lowercase.
    c51 = models.FloatField(db_column='C51', blank=True, null=True)  # Field name made lowercase.
    c52 = models.FloatField(db_column='C52', blank=True, null=True)  # Field name made lowercase.
    c53 = models.FloatField(db_column='C53', blank=True, null=True)  # Field name made lowercase.
    c54 = models.FloatField(db_column='C54', blank=True, null=True)  # Field name made lowercase.
    c55 = models.FloatField(db_column='C55', blank=True, null=True)  # Field name made lowercase.
    c56 = models.FloatField(db_column='C56', blank=True, null=True)  # Field name made lowercase.
    c57 = models.FloatField(db_column='C57', blank=True, null=True)  # Field name made lowercase.
    c58 = models.FloatField(db_column='C58', blank=True, null=True)  # Field name made lowercase.
    c59 = models.FloatField(db_column='C59', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CashFlowNonFin'

class Data(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    circulationstock = models.FloatField(db_column='CirculationStock', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=2, blank=True, null=True)  # Field name made lowercase.
    incometax = models.FloatField(db_column='IncomeTax', blank=True, null=True)  # Field name made lowercase.
    netprofit = models.FloatField(db_column='NetProfit', blank=True, null=True)  # Field name made lowercase.
    accountsreceivable = models.FloatField(db_column='AccountsReceivable', blank=True, null=True)  # Field name made lowercase.
    advancepayment = models.FloatField(db_column='AdvancePayment', blank=True, null=True)  # Field name made lowercase.
    stock = models.FloatField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.
    totalcurrentassets = models.FloatField(db_column='TotalCurrentAssets', blank=True, null=True)  # Field name made lowercase.
    fixedassets = models.FloatField(db_column='FixedAssets', blank=True, null=True)  # Field name made lowercase.
    intangibleassets = models.FloatField(db_column='IntangibleAssets', blank=True, null=True)  # Field name made lowercase.
    goodwill = models.FloatField(db_column='GoodWill', blank=True, null=True)  # Field name made lowercase.
    totalcapital = models.FloatField(db_column='TotalCapital', blank=True, null=True)  # Field name made lowercase.
    payableaccount = models.FloatField(db_column='PayableAccount', blank=True, null=True)  # Field name made lowercase.
    payableinterest = models.FloatField(db_column='PayableInterest', blank=True, null=True)  # Field name made lowercase.
    othercurrentliability = models.FloatField(db_column='OtherCurrentLiability', blank=True, null=True)  # Field name made lowercase.
    totalcurrentliability = models.FloatField(db_column='TotalCurrentLiability', blank=True, null=True)  # Field name made lowercase.
    longtermloan = models.FloatField(db_column='LongtermLoan', blank=True, null=True)  # Field name made lowercase.
    longtermpayable = models.FloatField(db_column='LongtermPayable', blank=True, null=True)  # Field name made lowercase.
    totalnoncurrentliability = models.FloatField(db_column='TotalNonCurrentLiability', blank=True, null=True)  # Field name made lowercase.
    totalliability = models.FloatField(db_column='TotalLiability', blank=True, null=True)  # Field name made lowercase.
    assetvalue = models.FloatField(db_column='AssetValue', blank=True, null=True)  # Field name made lowercase.
    cashpayment = models.FloatField(db_column='CashPayment', blank=True, null=True)  # Field name made lowercase.
    cashforinterest = models.FloatField(db_column='CashForInterest', blank=True, null=True)  # Field name made lowercase.
    depreciation = models.FloatField(db_column='Depreciation', blank=True, null=True)  # Field name made lowercase.
    amortization = models.FloatField(db_column='Amortization', blank=True, null=True)  # Field name made lowercase.
    longtermamortization = models.FloatField(db_column='LongtermAmortization', blank=True, null=True)  # Field name made lowercase.
    quickratio = models.FloatField(db_column='QuickRatio', blank=True, null=True)  # Field name made lowercase.
    totalcapitalratioofreturn = models.FloatField(db_column='TotalCapitalRatioOfReturn', blank=True, null=True)  # Field name made lowercase.
    assetratioofreturn = models.FloatField(db_column='AssetRatioOfReturn', blank=True, null=True)  # Field name made lowercase.
    volatility = models.FloatField(db_column='Volatility', blank=True, null=True)  # Field name made lowercase.
    netfixedassetsrate = models.FloatField(db_column='NetFixedAssetsRate', blank=True, null=True)  # Field name made lowercase.
    cnname = models.CharField(db_column='CNName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identification = models.CharField(db_column='Identification', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Data'

class Data_Result(models.Model):
    pass

class Finrationonfin(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    c4 = models.FloatField(db_column='C4', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7', blank=True, null=True)  # Field name made lowercase.
    c8 = models.FloatField(db_column='C8', blank=True, null=True)  # Field name made lowercase.
    c9 = models.FloatField(db_column='C9', blank=True, null=True)  # Field name made lowercase.
    c10 = models.FloatField(db_column='C10', blank=True, null=True)  # Field name made lowercase.
    c11 = models.FloatField(db_column='C11', blank=True, null=True)  # Field name made lowercase.
    c12 = models.FloatField(db_column='C12', blank=True, null=True)  # Field name made lowercase.
    c13 = models.FloatField(db_column='C13', blank=True, null=True)  # Field name made lowercase.
    c14 = models.FloatField(db_column='C14', blank=True, null=True)  # Field name made lowercase.
    c15 = models.FloatField(db_column='C15', blank=True, null=True)  # Field name made lowercase.
    c16 = models.FloatField(db_column='C16', blank=True, null=True)  # Field name made lowercase.
    c17 = models.FloatField(db_column='C17', blank=True, null=True)  # Field name made lowercase.
    c18 = models.FloatField(db_column='C18', blank=True, null=True)  # Field name made lowercase.
    c19 = models.FloatField(db_column='C19', blank=True, null=True)  # Field name made lowercase.
    c20 = models.FloatField(db_column='C20', blank=True, null=True)  # Field name made lowercase.
    c21 = models.FloatField(db_column='C21', blank=True, null=True)  # Field name made lowercase.
    c22 = models.FloatField(db_column='C22', blank=True, null=True)  # Field name made lowercase.
    c23 = models.FloatField(db_column='C23', blank=True, null=True)  # Field name made lowercase.
    c24 = models.FloatField(db_column='C24', blank=True, null=True)  # Field name made lowercase.
    c25 = models.FloatField(db_column='C25', blank=True, null=True)  # Field name made lowercase.
    c26 = models.FloatField(db_column='C26', blank=True, null=True)  # Field name made lowercase.
    c27 = models.FloatField(db_column='C27', blank=True, null=True)  # Field name made lowercase.
    c28 = models.FloatField(db_column='C28', blank=True, null=True)  # Field name made lowercase.
    c29 = models.FloatField(db_column='C29', blank=True, null=True)  # Field name made lowercase.
    c30 = models.FloatField(db_column='C30', blank=True, null=True)  # Field name made lowercase.
    c31 = models.FloatField(db_column='C31', blank=True, null=True)  # Field name made lowercase.
    c32 = models.FloatField(db_column='C32', blank=True, null=True)  # Field name made lowercase.
    c33 = models.FloatField(db_column='C33', blank=True, null=True)  # Field name made lowercase.
    c34 = models.FloatField(db_column='C34', blank=True, null=True)  # Field name made lowercase.
    c35 = models.FloatField(db_column='C35', blank=True, null=True)  # Field name made lowercase.
    c36 = models.FloatField(db_column='C36', blank=True, null=True)  # Field name made lowercase.
    c37 = models.FloatField(db_column='C37', blank=True, null=True)  # Field name made lowercase.
    c38 = models.FloatField(db_column='C38', blank=True, null=True)  # Field name made lowercase.
    c39 = models.FloatField(db_column='C39', blank=True, null=True)  # Field name made lowercase.
    c40 = models.FloatField(db_column='C40', blank=True, null=True)  # Field name made lowercase.
    c41 = models.FloatField(db_column='C41', blank=True, null=True)  # Field name made lowercase.
    c42 = models.FloatField(db_column='C42', blank=True, null=True)  # Field name made lowercase.
    c43 = models.FloatField(db_column='C43', blank=True, null=True)  # Field name made lowercase.
    c44 = models.FloatField(db_column='C44', blank=True, null=True)  # Field name made lowercase.
    c45 = models.FloatField(db_column='C45', blank=True, null=True)  # Field name made lowercase.
    c46 = models.FloatField(db_column='C46', blank=True, null=True)  # Field name made lowercase.
    c47 = models.FloatField(db_column='C47', blank=True, null=True)  # Field name made lowercase.
    c48 = models.FloatField(db_column='C48', blank=True, null=True)  # Field name made lowercase.
    c49 = models.FloatField(db_column='C49', blank=True, null=True)  # Field name made lowercase.
    c50 = models.FloatField(db_column='C50', blank=True, null=True)  # Field name made lowercase.
    c51 = models.FloatField(db_column='C51', blank=True, null=True)  # Field name made lowercase.
    c52 = models.FloatField(db_column='C52', blank=True, null=True)  # Field name made lowercase.
    c53 = models.FloatField(db_column='C53', blank=True, null=True)  # Field name made lowercase.
    c54 = models.FloatField(db_column='C54', blank=True, null=True)  # Field name made lowercase.
    c55 = models.FloatField(db_column='C55', blank=True, null=True)  # Field name made lowercase.
    c56 = models.FloatField(db_column='C56', blank=True, null=True)  # Field name made lowercase.
    c57 = models.FloatField(db_column='C57', blank=True, null=True)  # Field name made lowercase.
    c58 = models.FloatField(db_column='C58', blank=True, null=True)  # Field name made lowercase.
    c59 = models.FloatField(db_column='C59', blank=True, null=True)  # Field name made lowercase.
    c60 = models.FloatField(db_column='C60', blank=True, null=True)  # Field name made lowercase.
    c61 = models.FloatField(db_column='C61', blank=True, null=True)  # Field name made lowercase.
    c62 = models.FloatField(db_column='C62', blank=True, null=True)  # Field name made lowercase.
    c63 = models.FloatField(db_column='C63', blank=True, null=True)  # Field name made lowercase.
    c64 = models.FloatField(db_column='C64', blank=True, null=True)  # Field name made lowercase.
    c65 = models.FloatField(db_column='C65', blank=True, null=True)  # Field name made lowercase.
    c66 = models.FloatField(db_column='C66', blank=True, null=True)  # Field name made lowercase.
    c67 = models.FloatField(db_column='C67', blank=True, null=True)  # Field name made lowercase.
    c68 = models.FloatField(db_column='C68', blank=True, null=True)  # Field name made lowercase.
    c69 = models.FloatField(db_column='C69', blank=True, null=True)  # Field name made lowercase.
    c70 = models.FloatField(db_column='C70', blank=True, null=True)  # Field name made lowercase.
    c71 = models.FloatField(db_column='C71', blank=True, null=True)  # Field name made lowercase.
    c72 = models.FloatField(db_column='C72', blank=True, null=True)  # Field name made lowercase.
    c73 = models.FloatField(db_column='C73', blank=True, null=True)  # Field name made lowercase.
    c74 = models.FloatField(db_column='C74', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinRatioNonFin'


class Profitnonfin(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    c4 = models.FloatField(db_column='C4', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7', blank=True, null=True)  # Field name made lowercase.
    c8 = models.FloatField(db_column='C8', blank=True, null=True)  # Field name made lowercase.
    c9 = models.FloatField(db_column='C9', blank=True, null=True)  # Field name made lowercase.
    c10 = models.FloatField(db_column='C10', blank=True, null=True)  # Field name made lowercase.
    c11 = models.FloatField(db_column='C11', blank=True, null=True)  # Field name made lowercase.
    c12 = models.FloatField(db_column='C12', blank=True, null=True)  # Field name made lowercase.
    c13 = models.FloatField(db_column='C13', blank=True, null=True)  # Field name made lowercase.
    c14 = models.FloatField(db_column='C14', blank=True, null=True)  # Field name made lowercase.
    c15 = models.FloatField(db_column='C15', blank=True, null=True)  # Field name made lowercase.
    c16 = models.FloatField(db_column='C16', blank=True, null=True)  # Field name made lowercase.
    c17 = models.FloatField(db_column='C17', blank=True, null=True)  # Field name made lowercase.
    c18 = models.FloatField(db_column='C18', blank=True, null=True)  # Field name made lowercase.
    c19 = models.FloatField(db_column='C19', blank=True, null=True)  # Field name made lowercase.
    c20 = models.FloatField(db_column='C20', blank=True, null=True)  # Field name made lowercase.
    c21 = models.FloatField(db_column='C21', blank=True, null=True)  # Field name made lowercase.
    c22 = models.FloatField(db_column='C22', blank=True, null=True)  # Field name made lowercase.
    c23 = models.FloatField(db_column='C23', blank=True, null=True)  # Field name made lowercase.
    c24 = models.FloatField(db_column='C24', blank=True, null=True)  # Field name made lowercase.
    c25 = models.FloatField(db_column='C25', blank=True, null=True)  # Field name made lowercase.
    c26 = models.FloatField(db_column='C26', blank=True, null=True)  # Field name made lowercase.
    c27 = models.FloatField(db_column='C27', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfitNonFin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Guben(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    circulationstock = models.FloatField(db_column='CirculationStock', blank=True, null=True)  # Field name made lowercase.
    totalstock = models.FloatField(db_column='TotalStock', blank=True, null=True)  # Field name made lowercase.
    changereason = models.CharField(db_column='ChangeReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    circulationa = models.FloatField(db_column='CirculationA', blank=True, null=True)  # Field name made lowercase.
    circulationb = models.FloatField(db_column='CirculationB', blank=True, null=True)  # Field name made lowercase.
    circulationh = models.FloatField(db_column='CirculationH', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(max_length=5, blank=True, null=True)
    quarter = models.CharField(db_column='Quarter', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guben'


class List(models.Model):
    symbolnumber = models.CharField(db_column='SymbolNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cnname = models.CharField(db_column='CNName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enname = models.CharField(db_column='ENName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'list'
