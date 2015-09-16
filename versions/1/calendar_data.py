#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import click
from datetime import datetime

from utils import (
    convert_date,
    xhalfdays,
    xhalfdays_for_day,
)


class CalendarData(object):

    def __init__(self, start_date, end_date, period_legend, symbol_legend):
        self.period_legend = period_legend
        self.symbol_legend = symbol_legend
        self.start_date = start_date
        self.end_date = end_date
        self.days = {}
        self.start_datetime = datetime(
            start_date.year,
            start_date.month,
            start_date.day,
            9
        )
        self.end_datetime = datetime(
            end_date.year,
            end_date.month,
            end_date.day,
            17
        )
        for halfday in xhalfdays(self.start_datetime, self.end_datetime):
            self.days[halfday] = self.get_blank_activity()

    def get_blank_activity(self):
        return {
            'nature': None,
            'type': None,
            'verbose_type': 'empty',
        }

    # TODO: this means that periods and symbols overwrite each other
    # Is this OK?
    def add_activity(self, activity):
        if activity['nature'] == 'period':
            self.add_period(activity)
        elif activity['nature'] == 'symbol':
            self.add_symbol(activity)
        else:
            click.echo('unknown nature: {}'.format(activity['nature']), err=True)

    def add_period(self, period):
        start_day = convert_date(period['startmoment'])
        end_day = convert_date(period['finishmoment'])
        if end_day < self.start_datetime or start_day > self.end_datetime:
            return
        if start_day < self.start_datetime:
            start_day = self.start_datetime
        if end_day > self.end_datetime:
            end_day = self.end_datetime
        for halfday in xhalfdays(start_day, end_day):
            self.days[halfday] = {
                'nature': 'period',
                'type': period['type'],
                'verbose_type': self.period_legend.get(period['type']),
                'label': period.get('label'),
            }

    def add_symbol(self, symbol):
        day = convert_date(symbol['moment'])
        if day < self.start_datetime or day > self.end_datetime:
            return
        for halfday in xhalfdays_for_day(day):
            self.days[halfday] = {
                'nature': 'symbol',
                'type': symbol['type'],
                'verbose_type': self.symbol_legend.get(symbol['type']),
                'label': self.symbol_legend.get(symbol['type']),
            }

    def get_count_key(self, day_data):
        if day_data['nature'] is None:
            return 'empty'
        return '{}{}'.format(day_data['nature'], day_data['type'])

    def new_count_item(self, key, day_data):
        item = {
            'days': 0.5,
            'nature': day_data['nature'],
            'type': day_data['type'],
        }
        if day_data['nature'] == 'period':
            item['verbose_type'] = self.period_legend.get(day_data['type'])
        elif day_data['nature'] == 'symbol':
            item['verbose_type'] = self.symbol_legend.get(day_data['type'])
        return item

    def count_time_for_types(self):
        counts = {
            'empty': {
                'nature': 'empty',
                'verbose_type': 'empty',
                'days': 0
            },
        }
        for day in self.days:
            day_data = self.days[day]
            key = self.get_count_key(day_data)
            if key in counts:
                counts[key]['days'] += 0.5
            else:
                counts[key] = self.new_count_item(key, day_data)
        return counts

    def ordered_days(self):
        """ generator yielding tuple of (day, day data) on each loop
        """
        for day in sorted(self.days.keys()):
            yield day, self.days[day]

    def activity_ranges(self):
        """ return data in ranges
        """
        start_day = sorted(self.days.keys())[0]
        current_activity = self.days(start_day)
        for day, day_data in self.ordered_days:
            # if new day matches, increment count of current_activity
            # else yield current_activity and start a new one
            yield current_activity
