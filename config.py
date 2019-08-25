# Author: Robby Marver
# Contact: rmarver12@gmail.com
# 
# Configuration file for using this tool.


# Configuration and access keys for Twitter Devs.
# See Twitter Dev documentation for how to obtain your
# own keys. These keys belong to Robert Marver (@RMarver)
consumer_key = 'sH5wxlpmYFmQ9Ytle7ceqbMEL'
consumer_secret = 'ntJHELZvxe6P2SC0CoVCdf2jRJIoSAzo7dI2HXbJddl9xHxXp7'
access_key = '968218095582986241-TpqyxTfUtlAQYCeGGnH2w6eRWrBu6na'
access_secret = 'aShnbpSOtGZ3HGZ9igXLxDUuwuyE0rH6pHlbScJbsG7El'

# Directory of compiled files
compiled_dir = 'compiled/'

# Root directory for NCAA csv files
ncaa_root_dir = 'ncaa/'

# Our lads ncaa root url for queries
ncaa_root_url = 'http://www.ourlads.com/ncaa-football-depth-charts/roster/'

# Team names, codes, and ids
# These are how the teams are defined in the URLs of OurLads.
ncaa_team_codes = [
    # ACC
    'boston-college/90153:BOSTON COLLEGE EAGLES',
    'clemson/90314:CLEMSON TIGERS',
    'duke/90406:DUKE BLUE DEVILS',
    'florida-state/90544:FLORIDA STATE SEMINOLES:FSUFootball:squad',
    'georgia-tech/90613:GEORGIA TECH YELLOW JACKETS',
    'louisville/90958:LOUISVILLE CARDINALS',
    'miami/91073:MIAMI HURRICANES',
    'north-carolina/91395:NORTH CAROLINA TAR HEELS',
    'nc-state/91280: NORTH CAROLINA STATE WOLFPACK',
    'pittsburgh/91694:PITTSBURGH PANTHERS',
    'syracuse/91924:SYRACUSE ORANGE:CuseFootball:current-players',
    'virginia/92384:VIRGINIA CAVALIERS',
    'virginia-tech/92407:VIRGINIA TECH HOKIES',
    'wake-forest/92430:WAKE FOREST DEMON DEACONS',
    # SEC
    'alabama/89923:ALABAMA CRIMSON TIDE',
    'arkansas/89992:ARKANSAS RAZORBACKS',
    'auburn/90061:AUBURN TIGERS',
    'florida/90498:FLORIDA GATORS',
    'georgia/90590:GEORGIA BULLDOGS',
    'kentucky/90866:KENTUCKY WILDCATS:UKFootball:uk-players',
    'lsu/90981:LSU TIGERS:LSUfootball:nfl-tigers',
    'ole-miss/91602:MISSISSIPPI REBELS',
    'mississippi-state/91211:MISSISSIPPI STATE BULLDOGS',
    'missouri/91234:MISSOURI TIGERS:_CarolineHall:mizzou-football-players',
    'south-carolina/91832:SOUTH CAROLINA GAMECOCKS',
    'tennessee/91993:TENNESSEE VOLUNTEERS',
    'texas-am/92039:TEXAS A&M AGGIES',
    'vanderbilt/92361:VANDERBILT COMMODORES',
    # BIG-10
    'illinois/90705:ILLINOIS FIGHTING ILLINI',
    'indiana/90728:INDIANA HOOSIERS',
    'iowa/90751:IOWA HAWKEYES',
    'maryland/91027:MARYLAND TERRAPINS',
    'michigan/91119:MICHIGAN WOLVERINES:UMichFootball:current-student-athletes',
    'michigan-state/91142:MICHIGAN STATE SPARTANS',
    'minnesota/91188:MINNESOTA GOLDEN GOPHERS',
    'nebraska/91303:NEBRASKA CORNHUSKERS',
    'northwestern/91464:NORTHWESTERN WILDCATS',
    'ohio-state/91533:OHIO STATE BUCKEYES',
    'penn-state/91671:PENN STATE NITTANY LIONS',
    'purdue/91717:PURDUE BOILERMAKERS',
    'rutgers/91763:RUTGERS SCARLET KNIGHTS',
    'wisconsin/92545:WISCONSIN BADGERS:BadgerFootball:current-badgers',
    # BIG-12
    'baylor/90107:BAYLOR BEARS',
    'iowa-state/90774:IOWA STATE CYCLONES',
    'kansas/90797:KANSAS JAYHAWKS',
    'kansas-state/90820:KANSAS STATE WILDCATS',
    'oklahoma/91556:OKLAHOMA SOONERS',
    'oklahoma-state/91579:OKLAHOMA STATE COWBOYS',
    'tcu/91947:TCU HORNED FROGS:TCUFootball:funkytown16',
    'texas/92016:TEXAS LONGHORNS',
    'texas-tech/92062:TEXAS TECH RED RAIDERS',
    'west-virginia/92499:WEST VIRGINIA MOUNTAINEERS',
    # PAC-12
    'arizona/89946:ARIZONA WILDCATS',
    'arizona-state/89969:ARIZONA STATE SUN DEVILS',
    'california/90245:CALIFORNIA GOLDEN BEARS:CalFootball:pro-bears',
    'oregon/91625:OREGON DUCKS:oregonfootball:football-student-athletes',
    'oregon-state/91648:OREGON STATE BEAVERS:BeaverFootball:team',
    'stanford/91901:STANFORD CARDINAL:StanfordFball:stanfordnfl',
    'ucla/92223:UCLA BRUINS',
    'usc/92269:USC TROJANS:uscfootball:players-present',
    'utah/92292:UTAH UTES:Utah_Football:current-players',
    'washington/92453:WASHINGTON HUSKIES',
    'washington-state/92476:WASHINGTON STATE COUGARS']

# Root directory for NFL csv files
nfl_root_dir = 'nfl/'

# OurLads root url for queries
nfl_root_url = 'http://www.ourlads.com/nfldepthcharts/roster/'

# Team names and codes for the NFL
nfl_team_codes = [
    'SF: SAN FRANCISCO 49ERS',
    'CHI: CHICAGO BEARS', 
    'CIN: CINCINATTI BENGALS', 
    'BUF: BUFFALO BILLS', 
    'DEN: DENVER BRONCOS', 
    'CLE: CLEVELAND BROWNS', 
    'ARZ: ARIZONA CARDINALS', 
    'LAC: LOS ANGELES CHARGERS', 
    'KC: KANSAS CITY CHIEFS', 
    'IND: INDIANAPOLIS COLTS', 
    'DAL: DALLAS COWBOYS', 
    'MIA: MIAMI DOLPHINS', 
    'PHI: PHILADELPHIA EAGLES', 
    'ATL: ATLANTA FALCONS', 
    'NYG: NEW YORK GIANTS', 
    'JAX: JACKSONVILLE JAGUARS', 
    'NYJ: NEW YORK JETS', 
    'DET: DETROIT LIONS', 
    'GB: GREEN BAY PACKERS', 
    'CAR: CAROLINA PANTHERS', 
    'NE: NEW ENGLAND PATRIOTS', 
    'OAK: OAKLAND RAIDERS', 
    'LAR: LOS ANGELES RAMS', 
    'BAL: BALTIMORE RAVENS', 
    'WAS: WASHINGTON REDSKINS', 
    'NO: NEW ORLEANS', 
    'SEA: SEATTLE SEAHAWKS', 
    'PIT: PITTSBURGH STEELERS', 
    'TB: TAMPA BAY BUCCANEERS', 
    'HOU: HOUSTON TEXANS', 
    'TEN: TENNESSEE TITANS', 
    'MIN: MINNESOTA VIKINGS']