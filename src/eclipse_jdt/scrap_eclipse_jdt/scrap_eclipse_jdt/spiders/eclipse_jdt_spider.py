# -*- coding: utf-8 -*

import scrapy
from scrapy.shell import inspect_response

"""Scrap some data of some Eclipse JDT bug reports

Save the product, component, version, priority, assigned-to,
description, title, reported date, status, platform, target milestone,
author, modified date and bug id data of all 'resolved' (bug status),
'verified' (bug status), 'closed' (bug status) and 'fixed'
(resolution) Eclipse JDT bug reports. 
"""

class EcplipseJDTSpider(scrapy.Spider):
    """The Spider to scrap some Eclipse JDT bug reports"""
    name = "eclipse_jdt" # The identifier of the Spider
    # Below, there are the URLs from which we will start
    start_urls = [
        "https://bugs.eclipse.org/bugs/buglist.cgi?" + \
        "bug_status=RESOLVED&bug_status=VERIFIED&" + \
        "bug_status=CLOSED&limit=10000&offset=0&" + \
        "order=bug_id%20DESC&product=JDT&query_format=advanced&" + \
        "resolution=FIXED", 
        "https://bugs.eclipse.org/bugs/buglist.cgi?" + \
        "bug_status=RESOLVED&bug_status=VERIFIED&" + \
        "bug_status=CLOSED&limit=10000&offset=10000&" + \
        "order=bug_id%20DESC&product=JDT&query_format=advanced&" + \
        "resolution=FIXED",
        "https://bugs.eclipse.org/bugs/buglist.cgi?" + \
        "bug_status=RESOLVED&bug_status=VERIFIED&" + \
        "bug_status=CLOSED&limit=10000&offset=20000&" + \
        "order=bug_id%20DESC&product=JDT&query_format=advanced&" + \
        "resolution=FIXED"
    ]

    def parse(self, response):
        """Handles the responses related to each request made"""
        # Follow each bug report link
        # inspect_response(response, self) # Un-comment if needed
        for bug_report in response.xpath("//tr[contains(@class, " + \
           "'bz_bugitem')]/td/a/@href").extract():
            yield scrapy.Request(response.urljoin(bug_report),
                                 callback=self.bug_report)

    def bug_report(self, response):
        """Handles the responses related to each bug report"""
        # Below, some XPaths are used to get some relevant data
        product = response \
        .xpath("//td[@id='field_container_product']/text()") \
        .extract_first()
        component = response \
        .xpath("//td[@id='field_container_component']/text()") \
        .extract_first()
        version = response \
        .xpath("//th[@id='field_label_version']/../td/text()") \
        .extract_first()
        priority = response \
        .xpath("//label[@for='priority']/../../td/text()") \
        .extract_first()
        assigned_to = response \
        .xpath("//a[@href='page.cgi?id=fields.html#assigned_to']" + \
            "/../../td/span/span/text()") \
        .extract_first()        
        description = response \
        .xpath("//pre[@class='bz_comment_text']/text()") \
        .extract_first()
        title = response \
        .xpath("//div[@class='bz_alias_short_desc_container " + \
            "edit_form']/span/span/text()") \
        .extract_first()
        bug_id =  response.xpath("//div[@class='bz_alias_short_" + \
            "desc_container edit_form']/a/b/text()") \
        .extract_first()
        bug_status =  response.xpath("//span" + \
            "[@id='static_bug_status']/text()") \
        .extract_first()
        platform =  response.xpath("//th" + \
            "[@id='field_label_rep_platform']/../td/text()") \
        .extract_first()
        target_milestone =  response.xpath("//label" + \
            "[@for='target_milestone']/../../td/text()") \
        .extract_first()
        reported_date =  response.xpath("//td" + \
            "[@id='bz_show_bug_column_2']//tr[1]/td/text()") \
        .extract_first()
        reported_by =  response.xpath("//td[@id='bz_show_" + \
            "bug_column_2']//tr[1]/td/span/span/text()") \
        .extract_first()
        modified_date =  response.xpath("//td" + \
            "[@id='bz_show_bug_column_2']//tr[2]/td/text()") \
        .extract_first()
        # Then, we yield the relevant data
        yield {
            'product': product,
            'component': component,
            'version': version,
            'priority': priority,
            'assigned_to': assigned_to,
            'description': description,
            'title': title,
            'bug_id': bug_id,
            'bug_status': bug_status,
            'platform': platform,
            'target_milestone': target_milestone,
            'reported_date': reported_date,
            'reported_by': reported_by,
            'modified_date': modified_date
        }
