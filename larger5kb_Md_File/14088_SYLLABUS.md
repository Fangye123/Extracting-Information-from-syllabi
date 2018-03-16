SYLLABUS

    
    
    
    
    
    SMILEY: A WEB-BASED REMOTE SENSING DATA MINING SYSTEM
    
    Dr. William Perrizo, Longjun Chen, Dennis Amundson Computer Science
    Department North Dakota State University Fargo, ND 58102 {Perrizo,
    lchen, amundson}@plains.nodak.edu
    
    ABSTRACT
    Remote sensing imagery (RSI) data will be used by potentially
    millions of users, provided that there exists a good way to access and
    manipulate that data. Currently, the most common way to manipulate and
    analyze RSI data is through a GIS system. Usually this method of the
    GIS distribution (both the software and the data) is costly and slow.
    Furthermore, the cost of owning RIS data is very high. These problems
    may limit the application and usage of remote sensing data.  In this
    paper, we describe a novel architecture to access, distribute, and
    analyze the massive amount of RSI data in order to address the problems
    described above. This architecture utilizes the most recent Internet
    technology and provide a distributed multi-tier client/server
    architecture for accessing and analyzing RSI data. SMILEY, a WWW-based
    remote sensing imagery data mining system, provides a general interface
    to access, display, and manipulate various sets of satellite imagery
    data. Users, through any common WWW browser, can use virtually any
    computer platform at any location to do RSI data analyzing.  The
    distributed server architecture of SMILEY is scaleable so it can easily
    be upgraded to handle an increasing workload thus achieving a high
    degree of reliability.
    
    
    1. INTRODUCTION
    
    The Earth Observing System (EOS) [EOS93] is one of NASA's ongoing
    space- and ground-based measurement systems to provide sustained
    observations of the earth. The EOS consists of a series of
    polar-orbiting and low-inclination satellites.  Each satellite bears
    several sensors, for long-term global observations of the land surface,
    biosphere, solid Earth, atmosphere, polar ice, and oceans.  The Earth
    Observing System Data and Information System (EOSDIS) manages the data
    sets derived from NASA's earth science research satellites and field
    measurement programs [BAR91]. EOSDIS data is one kind of remote sensing
    imagery (RSI) data. Other RSI data include radar data and remote
    digital photography.  Initially, it was assumed that EOSDIS data would
    be accessed by a few hundred primary EOS earth science investigators
    and approximately 10,000 additional researchers to carry out basic
    global-change research [VET95]. Since EOSDIS data belongs to the
    public, non-research users such as educators, agribusinesses, community
    planners, transportation users, and others who want to access it should
    be able to do so. Thus, EOSDIS data could potentially be used by
    millions of individuals, if a good method exists to access and
    manipulate the data.  Currently, the common way to manipulate and
    analyze EOSDIS data is through a commercial geographic information
    system (GIS) system. A typical GIS system is a standalone software
    package which the user purchases for geographical data manipulation.
    The data sets, which the user wants to use, may be obtained either with
    the purchased GIS system used or bought through third parties. These
    methods of distributing the GIS software and data are costly and slow.
    These problems may limit the application and usage of remote sensing
    data.  In this paper, we provide a novel architecture for accessing,
    distributing, and analyzing the massive amounts of remote sensing
    imagery (RSI) data to address the problems described above. This
    architecture utilizes the most recent Internet technology and make use
    of a distributed multi-tier client/server architecture for flexible
    accessing and analyzing of RSI data.  The World Wide Web (WWW) is an
    attractive, easy to use vehicle that makes data available for
    heterogeneous clients. At the present time, WWW browsers are available
    for all major operating systems. Web browser provides us a good
    platform for one to use and manipulate RSI data retrieved throuh the
    WWW. Signature Mining & Interface Language for EOSDIS, Yet-another
    (SMILEY) is a powerful online imagery analyzer and viewer.  Figure 1
    shows a typical display of SMILEY.
    
    
    
    Figure 1. SMILEY screen snapshot
    
    SMILEY provides a general interface from the World Wide Web using
    Internet technology to access, display, and manipulate various sets of
    RSI data. Eventually, any computer platform from any location on the
    Internet may be used to do imagery data analyzing. SMILEY uses the
    client/server model to fully utilize the user's client machine's
    processing power for achieving quick respond times. Users can also do
    data mining operations based on individual pixel values in the image or
    apply band-oriented functions.  They can also use many predefined
    filters (transfer functions) to process the image being analyzed and
    even define their own filter functions.
    
    This paper analyses the structure and functionality of SMILEY.
    In section 2, we provide some background information about
    SMILEY.  The structure of SMILEY version 1.1 is described in section 3.
    The server and client data mining functions provided in the current
    version of SMILEY are discussed in section 4. The conclusion along with
    some suggested future enhancements of SMILEY are described in section 5.
    
    2. BACKGROUND
    
    2.1 Introduction to Remote Sensing Imagery
    
    Of all data used in spatial data analyzing, one of the most
    important is undoubtedly that provided by remote sensing.
    Through the use of satellites, we now have a continuing program of data
    acquisition for the entire world with time frames ranging from a couple
    of weeks to a matter of hours. Very importantly, we also have access to
    these remotely sensed images in digital form, allowing for rapid
    integration of the results of remote sensing analysis to spatial data
    analyzing tools like SMILEY.
    
    Remote sensing can be defined as any process which gathers
    information about an object, area, or phenomenon without
    actually being in contact with it. Given this rather general
    definition, the term remote sensing has come to be associated more
    specifically with the gauging of interactions between earth surface
    materials and electromagnetic (EM) energy.
    
    Sensors can be divided into two broad groupspassive and active.
    Passive sensors measure ambient levels of existing sources of
    energy, while active ones provide their own source of energy. The
    majority of remote sensing is done with passive sensors, for which the
    sun is the major energy source. An example of this type of sensing is
    airborne photographs which capture energy in the visible spectrum.
    While aerial photography is still a major form of remote sensing, newer
    solid technologies have extended capabilities for viewing in the
    visible and near-infrared wavelengths to include longer wavelengths
    (such as solar radiation) as well. By contrast, active sensors provide
    their own source of energy.  The most familiar form of this is flash
    photography. However, in environmental applications, the best example
    of this type of sensing is radar.
    
    When EM energy strikes a material, three types of interaction
    can follow:  reflection, absorption, and/or transmission. For
    remote sensing, our main concern is with the reflected portion since
    that is what is usually returned to the sensor system. The exact amount
    of reflected energy will vary, and will depend upon the nature of the
    material and where in the EM spectrum our measurement is being taken.
    If we look at the nature of this reflected component over a varied
    range of wavelengths, we can characterize the measurement as a spectral
    response pattern, which is sometimes called a signature.  A signature
    is a description of the degree of which EM energy is reflected in
    different regions of the spectrum. Finding distinctive spectrum
    response patterns is key to most procedures for computer-assisted
    interpretation of remotely sensed imagery. This task is non-trivial.
    Rather, the analyst must interpret the right combination of spectral
    bands along with the time of year at which distinctive patterns can be
    found for each of the information classes of interest. A good tool is
    needed to help correctly interpret the RSI data.
    
    2.2   WWW: an Overview
    
    As the popularity of the Internet increases, people are
    becoming more aware of its potential. The World Wide Web (WWW,
    or the web) is a product of the continuous search for innovative ways
    of sharing information resources among heterogeneous machines and
    platforms. The implementation of the Web follows a standard
    client-server model. In this model, a user on a client machine executes
    a program (i.e., a web browser) to connect to a remote server machine
    (the web server) where a document store is located.  A typical Web
    transaction takes place when the client submits a request to access a
    particular document within the store, which the server usually complies
    with by sending back a copy of the requested document.  Most documents
    on the web are defined using a document markup language called
    Hypertext Markup Language (HTML), which allows one to easily add
    hyper-links to the text, which link to other HTML documents, as well as
    to other types of media (such as graphic images). Web browsers are GUI
    in nature. Because of these attributes, the WWW has quickly gained
    great popularity among Internet users.  At the present time, web
    browsers are implemented on most major operating systems.  The typical
    transaction model of the web is shown in figure 2. The World Wide Web
    is a client/server application. The server hosts the HTML content and
    waits for a request by a client. When the server receives this request,
    it will send the requested document back to the client. The client has
    a WWW browser that is used to request, receive, and display the HTML
    document. Previously, an HTML document consists of mostly static text
    and/or image files which could be downloaded from the server when
    requested by the client. With the help of Common Gateway Interface
    (CGI) scripts, a mechanism that allows WWW servers to execute
    special-purpose programs to handle specific requests, HTML documents
    can now contain some dynamic information based on the clients special needs.
    
    
    While HTML and CGI were intended to add simple user
    interactivity to WWW server sites, they are also an important
    means of providing the user a simple GUI-like interface to a
    distributed application without having to install additional software
    into the users client machine. However, these tools are not enough to
    handle complicated data- mining tasks. The limited layout control for
    the GUI and the lack of continuous execution state on either the client
    or server sides indicate a need for more sophisticated set of tools.
    
    2.3 Java: a Brief Overview
    Java is a new object-oriented programming language. Originally
    developed by Sun Microsystems for hand-held electronic devices,
    Java was engineered to be small and platform-independent, making it
    well suited to apply to the Internet environment. Java itself is
    object-oriented, implemented especially for network computing
    applications. Java has many useful features. An important one is that
    Java source code can be compiled into a machine-independent format,
    which consists of the set virtual machine instructions and symbolic
    data, commonly referred to as byte-code. Upon execution, a Java
    interpreter acts as the virtual machine and will interpret this
    byte-code. Most sophisticated web browsers have Java interpreters
    embedded within them. Thus, Java byte-code can be downloaded along with
    the HTML file to a web client machine and be executed locally within
    the clients machine.
    
    2.4 Application domain of SMILEY SMILEY has a very wide application
    domain. It can be used in various scientific fields, such as precision
    agriculture [BRA74], environmental protection, volcanic activity
    analysis, Earth surface analysis, Earth science education, etc. Various
    kinds of data mining can involve tools and techniques such as neural
    networks, genetic algorithms, expert systems, database filters, etc.  -
    Precision Agriculture A large store of land-process data is collected
    from the LANDSAT series of earth observing satellites (part of EOS),
    and is currently stored at the USGS EROS Data Center located in South
    Dakota.  Agriculture scientists and farmers can use SMILEY to process
    data, track site-specific farms, and monitor crop yields. SMILEY is
    gaining visibility within many precision agriculture and agri-business
    concerns.  - Education The SMILEY analyzer and satellite imagery viewer
    will be used in several teaching and learning projects.  The Upper
    Midwest Aerospace Consortium (a five-state effort to provide leadership
    in the areas of Earth System Science) will be using it in its K-12
    education component. In that component, school children and young
    adults will be able to view and manipulate images showing various
    places of interest.  They will be able to do a wide range of
    interesting projects with the tool.  Some of these include: viewing
    their farm for vegetation quality during the growing season, searching
    for grasshopper infestations, watching the spring surface water
    situation for flooding, monitoring wetlands drainage, as well as a
    number of other projects. These possibilities are limited only by the
    imagination of the users.
    
    3. SMILEY ARCHITECTURE
    
    SMILEY which stands for Signature Miner & interface Language
    for EOSDIS, Yet- another and is an online tool for viewing and
    analyzing remote sensing imagery data.  Using current Internet
    distributed processing techniques (such as Java and the WWW), SMILEY is
    being designed for the use of many types of remote users, who could be
    operating on one of many types of different system platforms at any
    place in the world.
    
    In general, the SMILEY architecture extends the normal World
    Wide Web architecture using the Java-enabled classic
    client/server paradigm. SMILEY fully utilizes the advantages of
    distributed computing, by taking advantage of the user's client
    machine's processing power to achieve good response times. When a user
    accesses the SMILEY- enabled web site using a Java capable web browser
    (like Netscape or Microsoft's Internet Explorer), the browser will
    download a number of SMILEY applets into the user's client machine. The
    applets then contact the SMILEY server for a specific remote sensing
    imagery data set. The SMILEY server retrieves the required data set
    either from local disk or remotely from a SMILEY data server through a
    dedicated network. Before transferring imagery data to the client, the
    SMILEY server will cut out the snapshot needed by the client and
    pre-format imagery data for easy client handling. The applets perform
    image analysis and data mining functions with a user-selected view of
    the image on the client host. This provides performance directly
    relating to the processing power of the client machine.  Currently,
    most PCs running in typical businesses location and at individuals
    homes have the power and memory needed to run all functions that SMILEY
    provides. The whole structure of SMILEY is shown in Figure 3.
    
    
    Figure 3. SMILEY (V1.1) system architecture
    
    There are two kinds of main components which constitute SMILEY. One set
    of components are passive in nature (stores of data and procedures),
    while the rest are active.  The two passive components are:  - Data
    sets of satellite imagery (data store).  This data can consist of TM
    data sets or other type images, stored both locally (with respect to
    other components) as well as remotely (being accessible through a
    broadband network). Because the volume of the data store can be so
    massive in nature (one uncompressed band of a TM scene requires 44MB of
    storage, and normally one TM scene consists of 7 bands), it is likely
    that most data will be stored away from the active components. The data
    is stored in a hierarchical fashion, in descending order of
    popularity.  This allows hot (i.e.  heavily used) data to be stored
    relatively close to the active components for quick access. Data that
    is relatively cool in nature would probably be stored at a distant
    location, such as an archive host accessible via a high-speed network
    or a near-line jukebox of persistent storage.  - Set of stored
    procedures (proc store).  The main functionality of SMILEY is
    implemented as a set of procedures written in Java. These, along with
    other additional miscellaneous documents (like on-line help pages) and
    procedures, are stored in the proc store.  The active components are:
    - Remote WWW browser (or web browser).  It is expected that the remote
    user will have on his/her local system a web browser that is capable of
    executing the applets composing SMILEY (from the proc store). At the
    present time, most graphical web browsers have an embedded Java
    interpreter to allow seamless integration of applet execution with
    normal web browsing.  - WWW server (or Web server).  A WWW server is
    mainly used for transferring hypertext documents (written in HTML) from
    a central store to a WWW browser.  The server may also be used to
    transfer other types of documents (such as graphic files) and for
    execution of procedures (typically called CGI programs) to accomplish
    simple tasks (such as authentication, or dynamic file creation). SMILEY
    uses the web server for transferring data from the procedure store to
    the web browser at the remote site.  When a remote user invokes SMILEY,
    the applets that compose its functionality will be downloaded to the
    browser via the web server.  - SMILEY server The purpose of the SMILEY
    server is to catalog the items composing the data store and to transfer
    to remotely executing applets the necessary remote sensing data
    requested by them.  Many times, items within the data store are not
    formatted as the applets would like them. As a result, the SMILEY
    server needs additional functionality to perform simple
    graphics-oriented tasks (such as clipping and rotating of images,
    filtering out one or more bands of the original images, etc.)  The
    complexity of this server varies directly with the complexity of the
    data store.
    
    4. SMILEY SERVER AND CLIENT FUNCTIONALITIES
    
    SMILEY is programmed using Java for its primary language. As
    discussed in section 2.2, Java is an object-oriented language.
    It is platform-independent and designed for purposes of network
    computing.
    
    Figure 4. SMILEY (V1.1) software structure
    
    A diagram representing the general functionality of SMILEY is
    shown in Figure 4.  The functionality can be divided into two
    parts: client-side processes and server-side processes. The clients
    main functional purpose is to do image data mining processing and
    result visualization; the servers main purpose is to process user
    registration information and to process image data requests initiated
    from client processes. At present, most client machines have very
    powerful processing abilities.  To take advantage of this fact, SMILEY
    distributes its data mining calculation and visualization processing
    onto the client, in order to achieve faster response times, and to
    decrease the load on the server.  4.1 SMILEY Server Processes The
    SMILEY servers are responsible for accepting client requests,
    maintaining image data indices, retrieving and pre-formatting image
    data, and sending image data back to the requesting client. The
    functionality of the SMILEY server can be divided into three parts:
    request handling and dispatching, data indices managing, and data
    retrieving and pre- formatting. These functions do not necessarily need
    to be implemented on the same machine.  Dividing up the server
    functionality gives more flexibility for the server to cope with an
    increasing workload.
    
    4.1.1 SMILEY Server The SMILEY server uses the concurrent server
    technique; it can serve an increased workload with better efficiency
    than one single server can. The SMILEY server acts as a task
    dispatcher, as shown in Figure 5.  When the SMILEY server receives a
    client request, it will check the request against its internal dispatch
    table. When it finds the appropriate data server or other server (such
    as index server for browsing request) to answer this request, it will
    dispatch the task to this server and make itself available to handle
    next request.
    
    4.1.2 SMILEY Index Server
    The SMILEY index server is a special server that serves the
    clients browsing requests. In the SMILEY index server, the
    server keeps all data sets indexed in a hierarchical tree structure as
    shown in Figure 6.
    
    
    Figure 5. SMILEY server task dispatch diagram
    
    
    Figure 6. Data index hierarchy tree
    
    All supported remote sensing data types are represented as top-level
    branches within the tree. Under these, all available imagery data sets
    are stored in separate sub-tree.  With this organize of data, combined
    with SMILEY clients index browser rendering function, the user is able
    to find a particular imagery set quite easily. This structure is
    flexible in nature, which makes it easy to organize data within the
    server.
    
    4.1.3 SMILEY Data Server One SMILEY data server is designed to serve
    one specific imagery data type.  Because each remote sensing data has a
    different format and structure, and furthermore, each data set in the
    same data type has different parameters, procedures serving each
    specific data type are designed to increase flexibility, scalability,
    and maintainability.  When a SMILEY data server receives a request from
    the SMILEY server, it will analyze the request and retrieve the header
    file of the required data set. From the header file, the data server
    can retrieve the necessary information needed to handle this data
    request. After analyzing the header file, the SMILEY data server then
    retrieves the imagery data needed to fulfil the request (either the
    full iamge or snapshot), and then formats it into what the SMILEY
    client requires. The resulting image is then transferred to the SMILEY
    client that requests the data.
    
    4.1.4 Typical SMILEY Server Processing Scenario Summary When the SMILEY
    server receives a data request from a SMILEY client, the SMILEY server
    will parse that request. If the request is a browsing request, the
    request is the dispatched to the SMILEY index server. Otherwise, the
    request is dispatched to a corresponding SMILEY data server.  When the
    SMILEY index server is activated, it will parse the request, retrieve
    the indices which the SMILEY system currently provides, reformat the
    index entries or viewing purpose, and transfer them back to the SMILEY
    client.  When a SMILEY data server receives a request, it will first
    parse the request. If the request is for a full-screen request (which
    is used to display a overview of the whole image set), the data server
    will reformat imagery data according to the user screen size and
    transfer it back to client after doing some additional formatting. If
    the request is for a snapshot request, the data server just retrieve
    the detailed data and transfer it back to client.
    
    4.2 SMILEY Client Processes
    
    4.2.1 Image Data Browsing & Selection
    
    SMILEY version 1.1 supports TM, SPOT, AVHRR and digital photography
    (TIFF) data set formats. There can be many imagery data sets for each
    format taken for the same or different places at different times. This
    process enables the user to select a data type and browse the entire
    data store.  As shown in Figure 7, users can click to see information
    about the data set, such as image size, its geo-location, the date the
    image was taken, etc. This information helps the user select the data
    set that he is interested in.
    
    Figure 7. Image browsing and selection screen
    
    4.2.2 Snapshot Selection & Creation Many imagery data sets are very
    large in size. For example, a typical TM image scene covers
    approximately 110 miles by 110 miles of area and consists of
    approximately 6200 by 6200 pixels with a resolution of 28.5 meters per
    pixel. This size is too big for individual processing needs, since most
    users will only care about their own farms or towns.  Based on the
    position of a sliding window, which the user moves, SMILEY will make a
    snapshot of the image scene before transferring it back to the client.
    Not only does this process help save on network bandwidth and reduce
    response time, but the processing requirements of the client are also
    greatly reduced. A screen dump of this process is shown in Figure 8.
    
    Figure 8. Snapshot selection and creation screen
    
    A typical snapshot is 250 by 250 pixels in size, which covers an area
    of about 56 square kilometers using TM data. All the data mining and
    visualization functions are performed on the snapshot. Thus, the main
    requests that the client sends to the SMILEY server are snapshot data
    requests. When the user selects a snapshot area, the client will send
    the data request to the server, the server will then process the
    request, pass it along to the data server. After retrieving the
    snapshot data, the SMILEY server sends the requested data back to the
    client.  4.2.3 Transfer (image filter) Functions Transfer functions are
    a specialized set of image filtering/visualization functions.  The
    SMILEY system predefines several often-used image filters: linear
    filter, band filter, hybrid filter, etc.  SMILEY also provides a
    user-defined filter interface, so that the user can visually define his
    own filter. By applying filter functions to the image snapshot, the
    user can perform interactive data mining on this image and visualize
    the results. The user can also use transfer functions to find data
    signatures before applying band-oriented or pixel- oriented data mining
    functions and visually see those results.
    
    Figure 9. An sample screen of the transfer function interface
    
    4.2.4 Band Mining Functions Band mining functions are used to do data
    mining based on band data. As discussed in Section 2, bands of the TM
    image are selected to maximize their capabilities for detecting and
    monitoring different types of Earth resources. The user can use
    predefined formulas to explore a variety of information contained in
    the image snapshot.  These functions also provide an interface for the
    user to enter his own formulas to generate a virtual band and visualize
    it. As shown in Figure 10, the VI formula (G-B) uses TM band 4 as G
    (Green) and band 7 as B (Blue) to represent the vegetation index in the
    region. After calculation, SMILEY can visualize the results.
    
    Figure 10. An example screen of band mining functions
    
    4.2.5 Pixel Mining Functions Pixel mining functions are used to do data
    mining to detect some specific digital signatures within the image.
    These functions provide the major support of the data mining
    capabilities of SMILEY. The signatures allow the user to detect
    specific characteristics from the image snapshot which could represent
    some phenomenon in the land being sensed.  To define a signature, the
    user selects a specific value, as well as a tolerance, for each band
    constituting the image.  After the user specifies the signature, SMILEY
    will find the pixels that match the signature, and visualize the pixels
    after performing some additional operators (such as merge or isolate).
    SMILEY will also calculate various statistics of the mining operations,
    such as percentage of pixels within the image snapshot that matched the
    signature. Figure 11 shows an example of the pixel mining function
    screen snapshot in SMILEY.
    
    Figure 11. Pixel-oriented data mining screen in SMILEY
    
    4.2.6 Geo-statistical Estimation Functions Any type of remote sensed
    measurement has some resolution due to the hardwares physical
    limitations and the large area usually under consideration. Some
    statistical procedures [REK87] can help to achieve improved and more
    efficient measurement analysis. The Kriging algorithm is a type of
    statistical method used to predict unknown points based on the known
    measurements using the regionalized variable theory. It is basically an
    interpolation process using moving-weighted averages. With kriging, the
    resolution of spatial data can be enhanced. SMILEY Version 1.1
    implemented the semi- variance function as shown in figure 12.
    
    
    Figure 12. SMILEY geo-statistical implementation
    
    4.3 Scalability and Reliability Consideration
    	Currently, SMILEY (Ver. 1.1) is implemented at North Dakota
    	State University (NDSU) on a UltraSparc workstation running
    Solaris. All server components (the web server, SMILEY server, SMILEY
    directory server, and SMILEY data server), the data store, and the proc
    store are implemented on the same system. When client requests increase
    in number, or the data store increases in size, the performance of the
    server will degrade. To solve the performance limitation, a distributed
    server architecture can be used.  When handling a large WWW load, the
    processing will be distributed over a number of low-end systems,
    interconnected by a high-speed dedicated network, as shown in Figure
    13. This architecture will also provide higher reliability than a
    single server architecture could by using redundant servers.
    
    
    Figure 13. Distributed architecture of SMILEY
    
    5. CONCLUSION
    In this paper, we present the system architecture of SMILEY, a
    WWW-based remote sensing imagery data mining system that is
    currently available on the Internet (http://smiley.cs.ndsu.nodak.edu).
    SMILEY uses current Internet techniques such as Java and the World Wide
    Web to explore a novel method in accessing, distributing and
    manipulating massive remote sensing imagery data. It achieves platform
    independence and easy of use. The client/server model is used in SMILEY
    to achieve quick response times.  The current implementation of SMILEY
    is numbered version 1.1. In this version, the implementation is a Java
    applet which can only be used on the Internet. The data sets to be
    analyzed are all stored online in the SMILEY server. The storage
    capacity of the server and the variety of the data is limited by the
    server that we are using. The geo-reference system in the current
    SMILEY system is also pre-mature, which will limit the usage of SMILEY
    for the time being.  As third party GIS systems evolve, the
    functionality provided by them will also increase. To utilize the power
    of these systems and to avoid re-inventing the wheel, SMILEY will need
    to provide a two-way interfaces with other commonly used GIS systems,
    such as ARC INFO/VIEW, MAP INFO, or IDRISI. These GIS systems have
    already provided a very good geo-reference system which can be used by
    SMILEY. What GIS systems lack is a rich collection of data mining
    tools, which is exactly what SMILEY provides. With the interface,
    SMILEY can take advantage of the functionality of existing GIS systems.
    Users will be benefited with this type of interaction between SMILEY
    and other common GIS systems.
    
    Limited by Javas security features, the current SMILEY system
    cannot access any data stored locally on a client system (i.e.,
    the data which is stored in a users hard disk or CD-ROM). This may
    limit somewhat the usage of the SMILEY system. Two techniques are under
    review to solve this problem: a standalone SMILEY system and a plug-in
    add-on to SMILEY. Both techniques will solve the local disk-accessing
    problem; but both will have pros and cons. The stand-alone technique
    will lose all advantages of the applet version, such as easy
    maintenance, upgrading, and centralized control. The plug-in technique
    will keep the all applet advantages but will bring in multiple binary
    executable code problems. When considering what the main motivation was
    for developing the current SMILEY system (to explore a novel
    architecture to access, distribute and manipulating remote sensing
    imagery data over Internet), the plug-in technique seems likely to prevail.
    
    REFERENCE:
    
    [BAR91] B. Barkstrom, A preliminary EOSDIS user model, NASA Langley
    Research Center, 1991
    
    [BRA74] E. J. Brach, Measurement of agriculture crops by remote
    spectral techniques, Remote Sensing Earth Resources, Vol. 3, 1974
    
    [BUR80] Burgess, T. M., and R. Webster, Optimal interpolation and
    isarithmic mapping of soil properties. I. The semivariogram and
    punctual krigging.  Journal Soil Sci. 31:315-331, 1980
    
    [DAV77] David, M., Geostatistical ore reserve Est. Elsevier Publ, NY, 1977
    
    [DEE75] Deering, D. W., Rouse, J. W., Haas, R. H., and Schell, J. A.,
    Measuring forage production of grazing units from Landsat MSS data.
    Proceedings of 10th International Symposium on Remote Sensing of
    Environment, II, 1169-1178, 1975
    
    [ELE92] F. J. Eley, R. Granger, and L. Martin, Soil moisture: Modeling
    and monitoring for regional planning, National Hydrology Research
    Center, Saskatoon, Saskatchewan, 1992
    
    [ELK94] M. Elkington, R. Meyer, and G. McConaughy, Defining the
    architectural development of EOSDIS to facilitate extension to a wider
    data information system, Hughes Applied Info System, EOSDIS Core Syst.
    Proj Tech. Paper 194-00131. Apr. 1994
    
    [EOS93] EOS Ref. Handbook, National Aeronautics and Space
    Administration, Earth Science Support Office, Washington, DC, Mar. 1993
    
    [HUE88] Huete, A. R., A soil-adjusted vegetation index. Remote Sensing
    and the Environment 25, 53-70, 1988
    
    [JAC83] Jackson, R. D., Spectral indices in n-space. Remote Sensing and
    the Environment 13, 409-421, 1983
    
    [JOU78] Journel, A. G. and Ch. J. Huijbregets, Mining Geostatistics,
    Academic Press, New York, 1978
    
    [JUE97] P. Juell, Implementation Issues of NDSU WWW server, 5th Wksp on
    Enabling Tech:  Infrastructure for Collaborative Enterprises, Stanford,
    Cal., Jun. 1996
    
    [KRI66] Krige, D. G., Two-dimensional weighted moving average trend
    surface for ore evaluation. Journal S. Afr. Inst. Min. Metall.
    66:13-38, 1966
    
    [REK87] R. E. Knighton and R. J. Wagenet, Geo-statistical Estimation of
    Spatial Structure, Continuum Water Resources Institute, Vol.1 Jul.,
    1987
    
    [RON97] Ronald J. E., Idrisi Users Guide, Version 3.0, Clark Labs for
    Cartographic Technology and Geographic Analysis, June 1997
    
    [ROU73] Rouse, J. W. Jr., Haas, R. H., Schell, J. A. and Deering, D.
    W., Monitoring vegetation systems in the Great Plains with ERTS. Earth
    Resources Technology Satellite-1 Symposium, Goddard Space Flight
    Center, Washington D.C., 309-317, 1973
    
    [TML96] EROS data center, Thematic Mapper Landsat Data, available on
    Internet at URL : http://edcwww.cr.usgs.gov/glis/hyper/guide/landsat_tm
    
    [VET95] R. Vetter, et al, Accessing Earth System Science Data and
    Applications Through High-Bandwidth Networks, IEEE Journal on Selected
    Areas in Comm, V13:5, June 1995
    
    Partially supported by grants, NSF No. OSR-9553368 and DARPA No.
    DAAH04-96-1-0329.
    
    
    

* * *

#####  [
[smiley](http://www.cs.ndsu.nodak.edu/~perrizo/classes/index.html>Back</A>

|| <A HREF=) || [Perrizo's
Home](http://www.cs.ndsu.nodak.edu/~perrizo/index.html) || [NDSU
Home](http://www.cs.ndsu.nodak.edu) ]

* * *

perrizo@plains.nodak.edu

* * *

