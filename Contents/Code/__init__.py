ITV_CATCHUP = "http://www.itv.com/_data/xml/CatchUpData/CatchUp360/CatchUpMenu.xml"
ITV_FILTER = "//ITVCatchUpProgramme"
ITV_HUB_SHOWS = "http://www.itv.com/hub/shows"
ITV_HUB_FILTER = "//*[contains(@class, 'grid-list__item')]"



##########################################################################################
def Start():
    ObjectContainer.title1 = 'ITVHUB'

##########################################################################################
@handler('/video/itvhub', 'ITVHUB')
def MainMenu():
    oc = ObjectContainer(no_cache=True)
    Log('IM HERE')
    title = "ITV Catch-up"
    oc.add(DirectoryObject(key=Callback(Shows, title=title, url=ITV_CATCHUP, xpath=ITV_FILTER), title=title))
    title = "ITV Hub Shows"
    oc.add(DirectoryObject(key=Callback(HubShows, title=title, url=ITV_HUB_SHOWS, xpath=ITV_HUB_FILTER), title=title))
    Log('NOW HERE')

    return oc

##########################################################################################
@route('/video/itvhub/shows')
def Shows(title, url, xpath):
    oc = ObjectContainer(title2=title)
    # pageElement = HTML.ElementFromURL(url)
    # items = pageElement.xpath(xpath)
    Log('The log:')
    # Log(url)
    for program in XML.ElementFromURL(url).xpath(xpath):

        season = 1
        index = 0

        ProgrammeTitle = program.xpath('./ProgrammeTitle/text()')[0]
        ProgrammeMediaUrl = program.xpath('./ProgrammeMediaUrl/text()')
        AdditionalHeaderText = program.xpath('./AdditionalHeaderText/text()')
        AdditionalSynopsisText = program.xpath('./AdditionalSynopsisText/text()')
        Url = program.xpath('./Url/text()')[0]

        Log('ProgrammeTitle:')
        Log(ProgrammeTitle)
        Log('ProgrammeMediaUrl:')
        Log(ProgrammeMediaUrl)
        Log('AdditionalHeaderText:')
        Log(AdditionalHeaderText)
        Log('AdditionalSynopsisText:')
        Log(AdditionalSynopsisText)
        Log('URL:')
        Log(Url)

        oc.add(
            EpisodeObject(
                url=Url,
                title=ProgrammeTitle,
                index=index,
                season=season,
                thumb=Resource.ContentsOfURLWithFallback(ProgrammeMediaUrl),
                summary=AdditionalSynopsisText
            )
        )


    Log('Andrew')
    # Log(programs)

    return oc

##########################################################################################
@route('/video/itvhub/hubshows')
def HubShows(title, url, xpath):
    oc = ObjectContainer(title2=title)
    Log('made it')
    for program in HTML.ElementFromURL(url).xpath(xpath):

        Title = program.xpath('.//h3[contains(@class, "tout__title")]//text()')[0].strip()
        Log('Title:')
        Log(Title)

        Meta = program.xpath('.//p[contains(@class, "tout__meta")]//text()')[0].strip()
        Log('Meta:')
        Log(Meta)

        Summary = program.xpath('.//p[contains(@class, "tout__summary")]//text()')
        if Summary:
            Summary = Summary[0].strip()

        Log('Summary:')
        Log(Summary)

        Url = program.xpath('./a/@href')
        if Url:
            Url = Url[0]

        Log('URL:')
        Log(Url)

        Thumb = program.xpath('.//img[contains(@class, "fluid-media__media")]/@src')
        if Thumb:
            Thumb = Thumb[0]
        Log('Thumb:')
        Log(Thumb)

        # oc.add(
        #     EpisodeObject(
        #         url=Url,
        #         title=Title,
        #         index=index,
        #         season=season,
        #         thumb=Resource.ContentsOfURLWithFallback(ProgrammeMediaUrl),
        #         summary=AdditionalSynopsisText
        #     )
        # )


        oc.add(
            EpisodeObject(
                url=Url,
                title=Title,
                thumb=Resource.ContentsOfURLWithFallback(Thumb),
                summary=Summary
            )
        )

    return oc