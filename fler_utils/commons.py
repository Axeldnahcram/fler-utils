#!/usr/bin/env python
# coding: utf-8
"""
.. module:: albator-utils commons
Common function to retrieve the file content
"""

import os
import logzero
from typing import Dict
import json
import io
import pathlib
from pprint import pprint
# installed
import uvloop
import aioredis
from dotenv import load_dotenv, find_dotenv
import aiofiles
# custom
import sys
import os
import fler_utils.constants as cst
LOGGER = logzero.logger

def get_asset_root() -> Dict[str, str]:
    """
    :return: the different assets paths to get sql and csv directories
    :rtype: dictionnary
    """
    dir = pathlib.Path(__file__).parent.parent.parent
    pql_root = str(pathlib.PurePath(dir, 'ext_files/pkl'))
    csv_root = str(pathlib.PurePath(dir, 'ext_files/csv'))
    txt_root = str(pathlib.PurePath(dir, 'ext_files/txt'))
    gazetteer_en_root = str(pathlib.PurePath(dir, 'ext_files/csv/Gazetteer_ENG'))
    gazetteer_fr_root = str(pathlib.PurePath(dir, 'ext_files/csv/Gazetteer_FR'))
    json_root = str(pathlib.PurePath(dir, 'ext_files/json/'))
    trainingdatasets_root = str(pathlib.PurePath(dir, 'ext_files/trainingdatasets/'))
    dict = {}
    dict
    dict["pql_root"] = pql_root
    dict["csv_root"] = csv_root
    dict["txt_root"] = txt_root
    dict["gazetteer_en_root"] = gazetteer_en_root
    dict["gazetteer_fr_root"] = gazetteer_fr_root
    dict["json_root"] = json_root
    dict["trainingdatasets_root"] = trainingdatasets_root

    return dict

def get_file_content(cfg, name, gaztype = None):
    contents = {}
    if cst.CSV_ROOT in cfg:
        root_folder = cfg.get(cst.CSV_ROOT)
        csv_file = f"{root_folder}/{name}.csv"
        if os.path.isfile(csv_file):
            return csv_file
    if cst.PQL_ROOT in cfg:
        root_folder = cfg.get(cst.PQL_ROOT)
        pql_file = f"{root_folder}/{name}.pql"
        if os.path.isfile(pql_file):
             return pql_file
    if cst.TXT_ROOT in cfg:
        root_folder = cfg.get(cst.TXT_ROOT)
        txt_file = f"{root_folder}/{name}.txt"
        if os.path.isfile(txt_file):
            return txt_file
    if cst.JSON_ROOT in cfg:
        root_folder = cfg.get(cst.JSON_ROOT)
        txt_file = f"{root_folder}/{name}.json"
        if os.path.isfile(txt_file):
            return txt_file
    if cst.TRAININGDATASETS_ROOT in cfg:
        root_folder = cfg.get(cst.TRAININGDATASETS_ROOT)
        LOGGER.info(root_folder)
        txt_file = f"{root_folder}/{name}.csv"
        LOGGER.info(txt_file)
        if os.path.isfile(txt_file):
            return txt_file
    if name == 'gazetteer_en':
        root_folder = cfg.get('gazetteer_en_root')
        ret = []
        if gaztype is None:
            for i in os.listdir(root_folder):
                ret.append(f"{root_folder}/{i}")
        else:
            for i in os.listdir(f"{root_folder}/{gaztype}"):
                ret.append(f"{root_folder}/{gaztype}/{i}")
        return ret

    else:
        LOGGER.error("File named %s does not exist", name)

    return contents

def get_type_of_gazetteers(cfg,language: str='en'):
    """
    get the list of the different gazetteers available for a language
    :param language: name of the language, either en, fr for now
    :type language: string
    :return: list of all the different gazetteer
    :rtype: list
    """
    root_folder = cfg.get(f'gazetteer_{language}_root')
    list_gaz = os.listdir(root_folder)
    return list_gaz

if __name__ == "__main__":
    f = get_asset_root()
    LOGGER.info(f)
    g = get_file_content(f, "CoNLL2003/test")
    LOGGER.info(g)
