from pya3 import *
from pprint import pprint

# generate api key in https://ant.aliceblueonline.com/apps 
alice = Aliceblue(user_id='347073',
    api_key='hLUQC1yiRaXIsCyfsW775JtcpFzT9obCHF7TVh1FBnoYosurv9CLIA4KWAZ0RRHMWIXMrtRTFNlPUTg6WitSq6cRICLNutiATkhINUmL5aqxTLkCf9rF09ALPgKFFZff')


session = alice.get_session_id() # Get Session ID
print(session)
# if 'sessionID' not in session:
#     print(session["emsg"])
# else:
#     print(session)
'''
aliceblue not login in phone - {'userId': None, 'userData': None, 'encKey': None, 'apikey': None, 'stat': 'Ok', 'emsg': 'User does not login. Please login', 'loginType': None, 'version': None, 'fcmToken': None, 'imei': None, 'login': False}
aliceblue logged in in phone - {'stat': 'Ok', 'sessionID': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyam9lOFVScGxZU3FTcDB3RDNVemVBQkgxYkpmOE4wSDRDMGVVSWhXUVAwIn0.eyJleHAiOjE3MjM5NTM1OTYsImlhdCI6MTcyMDM0NjE3MCwianRpIjoiMWJlNTkyNzYtNDZjNS00MjJlLWE5NTMtMzRiMDkxOWVjZjdkIiwiaXNzIjoiaHR0cHM6Ly9hYjEuYW1vZ2EudGVjaC9hbXNzby9yZWFsbXMvQWxpY2VCbHVlIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImE3YWY2NzExLWQwYjktNDg4Ni04OGQ4LTc5ZmQ2Y2E5MjExYSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFsaWNlLWtiIiwic2Vzc2lvbl9zdGF0ZSI6ImM2ZWM0OTIyLWZlNTAtNDAxOC1iMDE3LTUyMjUwYTQxZmNkNyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2xvY2FsaG9zdDozMDAyIiwiaHR0cDovL2xvY2FsaG9zdDo1MDUwIiwiaHR0cDovL2xvY2FsaG9zdDo5OTQzIiwiaHR0cDovL2xvY2FsaG9zdDo5MDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtYWxpY2VibHVla2IiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFsaWNlLWtiIjp7InJvbGVzIjpbIkdVRVNUX1VTRVIiLCJBQ1RJVkVfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwic2lkIjoiYzZlYzQ5MjItZmU1MC00MDE4LWIwMTctNTIyNTBhNDFmY2Q3IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInVjYyI6IjM0NzA3MyIsImNsaWVudFJvbGUiOlsiR1VFU1RfVVNFUiIsIkFDVElWRV9VU0VSIl0sIm5hbWUiOiJBU0hJU0ggREhBR0UiLCJtb2JpbGUiOiI4OTA0Mjc1MjI1IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiMzQ3MDczIiwiZ2l2ZW5fbmFtZSI6IkFTSElTSCIsImZhbWlseV9uYW1lIjoiREhBR0UiLCJlbWFpbCI6ImFzaGlzaGFuaWxkaGFnZUBnbWFpbC5jb20ifQ.fPd0CcP1Lg-r-OXMf1jWQ5HQ5XQYlpf8cCzr51ROTRhp5GwG8P6zt92Auryxcq4_nCj2y9UehKmnD_1MuZtaFm3_gqvGZ7Un11plCDfAOJvpDrosqJF4pmmtPziKczB_fWScOkR3Mxf2kiDum8Q1Mp4BZrUgS5woGMKjyMMoRDtWaKsxryBkDlGrhxiLVuhPm0PFlLa-X9ASjIOhe9X1WXmpRcVWBeBMq6x6djlZyYeW0FqrV9-PAvkMoJAgzBDKShMvBq2bqAQttJggtho4a1hD-w9ffLAXJSDaqe5rJBEJMFvvYnpRyRs11rCubJWJXmajiqzZ7Lo-Gv3nbfgNaQ'}
wrong user_id - {'userId': None, 'userData': None, 'encKey': None, 'apikey': None, 'stat': 'Ok', 'emsg': 'API key not available. Please generate API key', 'loginType': None, 'version': None, 'fcmToken': None, 'imei': None, 'login': False}
wrong api_key - {'stat': 'Not ok', 'emsg': 'Invalid Input'}
'''



# pprint(alice.get_balance()) # get balance / margin limits
# ''' 
# [{'adhocMargin': '0.00',
#   'adhocscripmargin': '0.00',
#   'branchAdhoc': '0.000000',
#   'brokeragePrsnt': '0.00',
#   'cashmarginavailable': '0.00',
#   'category': 'ABFSFREEDOM',
#   'cdsSpreadBenefit': '0',
#   'cncBrokeragePrsnt': '0.00',
#   'cncMarginUsed': '0.00',
#   'cncRealizedMtomPrsnt': '0',
#   'cncSellCrditPrsnt': '0',
#   'cncUnrealizedMtomPrsnt': '0.00',
#   'collateralvalue': '0.00',
#   'coverOrderMarginPrsnt': '0.00',
#   'credits': '0.00',
#   'debits': '0.00',
#   'directcollateralvalue': '0.00',
#   'elm': '0.00',
#   'exchange': 'ALL',
#   'exposuremargin': '0.00',
#   'grossexposurevalue': '0.00',
#   'losslimit': '0',
#   'mfamount': '0.00',
#   'mfssAmountUsed': '0.00',
#   'multiplier': '1.00',
#   'net': '0.00',
#   'nfoSpreadBenefit': '0',
#   'notionalCash': '0.000000',
#   'payoutamount': '0.00',
#   'premiumPrsnt': '0.00',
#   'product': 'ALL',
#   'realizedMtomPrsnt': '0.00',
#   'rmsIpoAmnt': '0',
#   'rmsPayInAmnt': '0.00',
#   'scripbasketmargin': '0.00',
#   'segment': 'ALL',
#   'spanmargin': '0.00',
#   'stat': 'Ok',
#   'subtotal': '0.00',
#   'symbol': 'ALL',
#   'turnover': '0.00',
#   'unrealizedMtomPrsnt': '0.00',
#   'valueindelivery': '0',
#   'varmargin': '0.00'}]
#  '''

# pprint(alice.get_profile()) # get profile
# ''' 
# {'accountId': '347073',
#  'accountName': 'ASHISH ANIL DHAGE',
#  'accountStatus': 'Activated',
#  'cellAddr': '8904275225',
#  'dpType': 'NA',
#  'emailAddr': 'ASHISHANILDHAGE@GMAIL.COM',
#  'exchEnabled': 'bse_cm|bse_fo|bcs_fo|cde_fo|mcx_fo|nse_cm|nse_fo|',
#  'product': ['CNC', 'NRML', 'MIS', 'MTF', 'CO', 'BO'],
#  'sBrokerName': 'ALICEBLUE'}
#  '''

# get_balance_response=alice.get_balance()
# pprint(Alice_Wrapper.get_balance(get_balance_response))
# '''
# {'data': {'cash_positions': [{'available': {'adhoc_margin': '0.00',
#                                             'cashmarginavailable': '0.00',
#                                             'collateral_value': '0.00',
#                                             'credits': '0.00',
#                                             'direct_collateral_value': '0.00',
#                                             'notionalCash': '0.000000',
#                                             'pay_in': '0.00'},
#                               'category': 'ABFSFREEDOM',
#                               'net': '0.00',
#                               'segment': 'ALL',
#                               'utilized': {'debits': '0.00',
#                                            'elm': '0.00',
#                                            'exposure_margin': '0.00',
#                                            'multiplier': '1.00',
#                                            'pay_out': '0.00',
#                                            'premium_present': '0.00',
#                                            'realised_m2m': '0.00',
#                                            'span_margin': '0.00',
#                                            'unrealised_m2m': '0.00',
#                                            'var_margin': '0.00'}}]},
#  'message': '',
#  'status': 'success'}
# '''

# get_profile_response=alice.get_profile()
# pprint(Alice_Wrapper.get_profile(get_profile_response))
# '''
# {'data': {'backoffice_enabled': None,
#           'banks': [],
#           'broker_name': 'ALICEBLUE',
#           'dp_ids': [],
#           'email_address': 'ASHISHANILDHAGE@GMAIL.COM',
#           'exchanges': ['BSE', 'BSE', 'BCS', 'CDE', 'MCX', 'NSE', 'NSE'],
#           'login_id': '347073',
#           'name': 'ASHISH ANIL DHAGE',
#           'pan_number': '',
#           'phone': '8904275225'},
#  'message': '',
#  'status': 'success'}
# '''

# print(alice.get_instrument_by_symbol('NSE','ONGC'))

# all_sensex_scrips = alice.search_instruments('NSE', 'TATA')
# pprint(all_sensex_scrips)
# '''
# [Instrument(exchange='NSE', token='21190', symbol='SERENCD8.40%SR.IICI&II', name='TATACAP-N5', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21192', symbol='SERENCD8.50%SR.IICIII&IV', name='TATACAP-N6', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21194', symbol='SERENCD8.55%SR.IIICI&II', name='TATACAP-N7', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21197', symbol='SERENCD8.65%SR.IIICIII&IV', name='TATACAP-N8', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21221', symbol='UNSERENCD9.00%SRIIICI&II', name='TATACAP-N9', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21225', symbol='UNSERENCD9.1%SRIIICIII&IV', name='TATACAP-NA', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21227', symbol='UNSERENCD8.75%SR.IVCI&II', name='TATACAP-NB', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21229', symbol='UNSERENCD8.85%SRIVCIII&IV', name='TATACAP-NC', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='22643', symbol='TATA CAP 7.99% 2034 SR A', name='TATACAP-ND', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='22684', symbol='TATA CAP 7.99% 2029 SR B', name='TATACAP-NE', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='22919', symbol='TCL 8.285% 2027 SR C', name='TATACAP-NF', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16870', symbol='SEC RED NCD 8.10% SR.IV', name='TATACAPHSG-N8', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='23246', symbol='TCHFL 7.92% 2034 SR E', name='TATACAPHSG-NF', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16872', symbol='SEC RED NCD 8.30% SR.V', name='TATACAPHSG-N9', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16874', symbol='SEC RED NCD 8.40% SR.V', name='TATACAPHSG-NA', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16894', symbol='UN SE RE NCD 8.55% SR.VI', name='TATACAPHSG-NB', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='20786', symbol='TCHFL 8.0409% 2027 SR.C', name='TATACAPHSG-NC', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='22768', symbol='TCHFL 8.10% 2027 SR D', name='TATACAPHSG-ND', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16838', symbol='SEC RED NCD 8.01% SR.IV', name='TATACAPHSG-N7', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16836', symbol='SEC RED NCD 8.30% SR.III', name='TATACAPHSG-N6', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16834', symbol='SEC RED NCD 8.20% SR.III', name='TATACAPHSG-N5', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16791', symbol='SEC RED NCD 8.01% SR.II', name='TATACAPHSG-N4', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16789', symbol='SEC RED NCD 7.92% SR.II', name='TATACAPHSG-N3', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3405', symbol='TATA CHEMICALS LTD', name='TATACHEM-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3721', symbol='TATA COMMUNICATIONS LTD', name='TATACOMM-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='23279', symbol='TATA COMMUNICATIONS LTD', name='TATACOMM-T0', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3432', symbol='TATA CONSUMER PRODUCT LTD', name='TATACONSUM-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3411', symbol='TATA ELXSI LIMITED', name='TATAELXSI-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21401', symbol='TATAAML-TATAGOLD', name='TATAGOLD-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='6636', symbol='TATA INVESTMENT CORP LTD', name='TATAINVEST-BE', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3456', symbol='TATA MOTORS LIMITED', name='TATAMOTORS-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='16965', symbol='TATA MOTORS DVR  A  ORD', name='TATAMTRDVR-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3426', symbol='TATA POWER CO LTD', name='TATAPOWER-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='3499', symbol='TATA STEEL LIMITED', name='TATASTEEL-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='20293', symbol='TATA TECHNOLOGIES LIMITED', name='TATATECH-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='7838', symbol='TATAAML - NETF', name='NETF-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='12978', symbol='TATAAML - NPBET', name='NPBET-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='21428', symbol='TATAAML-TATSILV', name='TATSILV-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='11536', symbol='TATA CONSULTANCY SERV LT', name='TCS-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='8882', symbol='TATAAML - TNIDETF', name='TNIDETF-EQ', expiry=None, lot_size='1'),
#  Instrument(exchange='NSE', token='8954', symbol='TATA TELESERV(MAHARASTRA)', name='TTML-EQ', expiry=None, lot_size='1')]
# '''

# # TransactionType.Buy, OrderType.Market, ProductType.Delivery
# print(alice.place_order(transaction_type = TransactionType.Buy, # , TransactionType.Buy, TransactionType.Sell
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'), # NSE, BSE (for now)
#                      quantity = 1, # 1 or above only
#                      order_type = OrderType.Market, 
#                      # OrderType.Market, OrderType.Limit, OrderType.StopLossMarket, OrderType.StopLossLimit
#                      product_type = ProductType.Delivery,
#                      # ProductType.Delivery, ProductType.Intraday, ProductType.CoverOrder, ProductType.BracketOrder
#                      price = 0.0, # 0.0, float
#                      trigger_price = None, #None, float
#                      stop_loss = None, #None, float
#                      square_off = None, #None, float
#                      trailing_sl = None, #None, int (for points trailing)
#                      is_amo = False, # True, False
#                      order_tag='order1'))
# '''
# {'stat': 'Ok', 'NOrdNo': '24070300385863'}
# '''

# # TransactionType.Buy, OrderType.Market, ProductType.Delivery
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.Market,
#                      product_type = ProductType.Delivery,
#                      price = 0.0,
#                      trigger_price = None,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
#    )

# # TransactionType.Buy, OrderType.Market, ProductType.Intraday
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.Market,
#                      product_type = ProductType.Intraday,
#                      price = 0.0,
#                      trigger_price = None,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.Market, ProductType.CoverOrder
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.Market,
#                      product_type = ProductType.CoverOrder,
#                      price = 0.0,
#                      trigger_price = 7.5, # trigger_price Here the trigger_price is taken as stop loss (provide stop loss in actual amount)
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.Limit, ProductType.BracketOrder
# # OCO Order can't be of type market
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.Limit,
#                      product_type = ProductType.BracketOrder,
#                      price = 8.0,
#                      trigger_price = None,
#                      stop_loss = 6.0,
#                      square_off = 10.0,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.Limit, ProductType.Intraday
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.Limit,
#                      product_type = ProductType.Intraday,
#                      price = 8.0,
#                      trigger_price = None,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )


# # TransactionType.Buy, OrderType.Limit, ProductType.CoverOrder
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.Limit,
#                      product_type = ProductType.CoverOrder,
#                      price = 7.0,
#                      trigger_price = 6.5, # trigger_price Here the trigger_price is taken as stop loss (provide stop loss in actual amount)
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.StopLossMarket, ProductType.Delivery
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.StopLossMarket,
#                      product_type = ProductType.Delivery,
#                      price = 0.0,
#                      trigger_price = 8.0,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.StopLossMarket, ProductType.Intraday
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.StopLossMarket,
#                      product_type = ProductType.Intraday,
#                      price = 0.0,
#                      trigger_price = 8.0,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.StopLossMarket, ProductType.CoverOrder
# # CO order is of type Limit and And Market Only

# # TransactionType.Buy, OrderType.StopLossMarket, ProductType.BO
# # BO order is of type Limit and And Market Only

# # TransactionType.Buy, OrderType.StopLossLimit, ProductType.Delivery
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.StopLossMarket,
#                      product_type = ProductType.Delivery,
#                      price = 8.0,
#                      trigger_price = 8.0,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.StopLossLimit, ProductType.Intraday
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.StopLossLimit,
#                      product_type = ProductType.Intraday,
#                      price = 8.0,
#                      trigger_price = 8.0,
#                      stop_loss = None,
#                      square_off = None,
#                      trailing_sl = None,
#                      is_amo = False,
#                      order_tag='order1')
# )

# # TransactionType.Buy, OrderType.StopLossLimit, ProductType.CoverOrder
# # CO order is of type Limit and And Market Only

# # TransactionType.Buy, OrderType.StopLossLimit, ProductType.BracketOrder
# print(
#    alice.place_order(transaction_type = TransactionType.Buy,
#                      instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
#                      quantity = 1,
#                      order_type = OrderType.StopLossLimit,
#                      product_type = ProductType.BracketOrder,
#                      price = 8.0,
#                      trigger_price = 8.0,
#                      stop_loss = 1.0,
#                      square_off = 1.0,
#                      trailing_sl = 20,
#                      is_amo = False,
#                      order_tag='order1')
# )





