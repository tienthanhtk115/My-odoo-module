# -*- coding: utf-8 -*-

from odoo import models, fields


class MapWebsite(models.Model):
    _name = 'map.website'
    _description = 'Map Website'

    name = fields.Char(string='Map Website Name', required=True)
    address_url = fields.Char(
        string='URL that uses the address',
        help="In this URL, {ADDRESS} will be replaced by the address.")
    lat_lon_url = fields.Char(
        string='URL that uses latitude and longitude',
        help="In this URL, {LATITUDE} and {LONGITUDE} will be replaced by "
        "the latitude and longitude (requires the module 'base_geolocalize')")
    route_address_url = fields.Char(
        string='Route URL that uses the addresses',
        help="In this URL, {START_ADDRESS} and {DEST_ADDRESS} will be "
        "replaced by the start and destination addresses.")
    route_lat_lon_url = fields.Char(
        string='Route URL that uses latitude and longitude',
        help="In this URL, {START_LATITUDE}, {START_LONGITUDE}, "
        "{DEST_LATITUDE} and {DEST_LONGITUDE} will be replaced by the "
        "latitude and longitude of the start and destination adresses "
        "(requires the module 'base_geolocalize').")
