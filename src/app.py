##
# @file app.py
# @author Yanis ATTIA (@yadev83)
# @brief The main app file for the covid-python application
# @version 0.1
# @date 2021-01-08
#
# @copyright Copyright (c) 2021
##

import request as req

api = req.Request()

api.getAllData()
api.printResponse()