#matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import requests

from pymongo import MongoClient
# client = MongoClient()
# client = MongoClient('138.197.131.70', 27017)
#
# db = client.busroutes
# collection = db.users
#
#
# post =  {}
# print(list(db.test.find()))
client = MongoClient("138.197.131.70", 27017, maxPoolSize=50)
db = client.busroutes
collection = db['users']
cursor = collection.find({})
for document in cursor:
    print(document)


data = np.array([[51.0459659018231, -114.0691813769432],
[51.04608435570873, -114.0694345325367],
[51.045316767126614, -114.06921299514872],
[51.0455425456566, -114.06940238852654],
[51.046433836323004, -114.0692105977606],
[51.04509410504732, -114.06914320842532],
[51.045643261975805, -114.06914622541929],
[51.045329796752185, -114.06912275251725],
[51.04556777961309, -114.06934689830449],
[51.04524150760099, -114.06915922780453],
[51.04628915597472, -114.06922498489773],
[51.046208726684696, -114.06923257635779],
[51.04574138888756, -114.06933906662525],
[51.04500357577299, -114.06931344122474],
[51.046085870918375, -114.06942703886615],
[51.04491428340675, -114.0694258356322],
[51.04578131325951, -114.06921732151821],
[51.04531365463301, -114.06916979886971],
[51.04642721439166, -114.06919843534429],
[51.04629965559577, -114.06922083014713],
[51.04633005426945, -114.06916783297844],
[51.04631170668994, -114.06937964946857],
[51.045241196796184, -114.06915975623947],
[51.045106656972656, -114.06918484245432],
[51.046280689854626, -114.0692850244196],
[51.04519769907109, -114.06939420374476],
[51.04655376883392, -114.0692790408506],
[51.04616467625475, -114.06918010154088],
[51.045283887680284, -114.06932393783407],
[51.04640633185873, -114.06911794363003],
[51.04639752983692, -114.06926666306147],
[51.045409056033, -114.0692788329299],
[51.0452828838437, -114.06917694320298],
[51.04561259613494, -114.06927175860831],
[51.04615870780259, -114.06929344330605],
[51.04496501428251, -114.06927717648941],
[51.04619335216964, -114.06933707342301],
[51.046333899416325, -114.0692765902919],
[51.04633496236098, -114.06939127670523],
[51.046300470907525, -114.06918775315353],
[51.045109340558845, -114.06914826595379],
[51.045567747068326, -114.0692943665667],
[51.04499781064483, -114.06924955855746],
[51.04541739376424, -114.0692206617948],
[51.045390699621045, -114.06915679242924],
[51.04636621821797, -114.0692170065547],
[51.04493772763672, -114.06934668842128],
[51.04583852624058, -114.06939668758758],
[51.046110679474374, -114.06934415755246],
[51.045024723917436, -114.06934827762582],
[51.04623822123438, -114.06910993408258],
[51.04506361077173, -114.06919450295526],
[51.045018620934776, -114.06938374844808],
[51.046463786296314, -114.06918128567385],
[51.0464114331062, -114.06940693663671],
[51.04569647064132, -114.06926764252574],
[51.04537991637173, -114.06940951575302],
[51.04597182677698, -114.06918837999336],
[51.046454066054714, -114.0693861379092],
[51.04605256409899, -114.06926903321634],
[51.04538466595132, -114.06935496773556],
[51.04558420151124, -114.06910225392915],
[51.04605368832883, -114.06926941150398],
[51.04502287341491, -114.06915086075696],
[51.046305705741275, -114.06930675856151],
[51.04585997274394, -114.06915302257592],
[51.04618771664595, -114.06928617874152],
[51.04626124286336, -114.06918155390346],
[51.04512993269037, -114.06910315216943],
[51.045887153939596, -114.06928805877946],
[51.04493862719252, -114.0693002906656],
[51.04546552824289, -114.06933966754524],
[51.04525010242863, -114.06910564279944],
[51.045012417055695, -114.0692273687193],
[51.04563219699548, -114.0691229574448],
[51.04547017147452, -114.06934644601243],
[51.04488952633062, -114.06917001350652],
[51.04541050066186, -114.06936928823434],
[51.04496782497164, -114.06941900634033],
[51.04574706395451, -114.06913684780486],
[51.04635634251301, -114.06929311399803],
[51.04639580627077, -114.06937928125143],
[51.04531823490589, -114.06924374962979],
[51.04498081110828, -114.06913881299425],
[51.044935287633805, -114.06913363882609],
[51.046016922340165, -114.06912062149057],
[51.0459001096523, -114.06923374355885],
[51.04567576229876, -114.06930055456051],
[51.046565144306086, -114.06936718746697],
[51.04515906324736, -114.06927573871216],
[51.045754458486925, -114.06943671966197],
[51.04499741865135, -114.06915965486452],
[51.04631029087768, -114.06914988726433],
[51.04635366193557, -114.06926501081092],
[51.045224767924246, -114.06925596974628],
[51.04489508273015, -114.06909774862348],
[51.04530302837677, -114.06935886068378],
[51.04511360457685, -114.06927178288032],
[51.04515623665051, -114.06933046572446],
[51.04582486258884, -114.0693985734916],
[51.04594561131058, -114.06917581802219],
[51.04489584534563, -114.06933639467842],
[51.04520064574916, -114.06923799550036],
[51.0458813942982, -114.0691451695783],
[51.04512715738739, -114.06929405687319],
[51.045962389686224, -114.06940399753904],
[51.04650166452371, -114.06927059632129],
[51.04510189564138, -114.06931400919426],
[51.04564286224374, -114.06914314956676],
[51.04529288425841, -114.069308942167],
[51.04544864328648, -114.06930956663975],
[51.04649341444753, -114.0692018379445],
[51.0459201952906, -114.06917559985574],
[51.04536730208627, -114.06931251845118],
[51.04538619314818, -114.06943733790058],
[51.045766384963365, -114.06931500855383],
[51.04639400156209, -114.06922175010092],
[51.04586346079801, -114.06931682857235],
[51.04616810447284, -114.06926948745812],
[51.04541485510218, -114.06934108862319],
[51.045602686312016, -114.06931322016841],
[51.04634536264947, -114.06926357466031],
[51.04622340381413, -114.06944017378521],
[51.04622399875572, -114.06934452349469],
[51.046192907718215, -114.06931315933431],
[51.04522559438653, -114.06935654230018],
[51.04555160111364, -114.06930027533551],
[51.0457937752997, -114.06917013563141],
[51.046498453164766, -114.06910959241864],
[51.04492327503357, -114.06934856098614],
[51.045412426989905, -114.06924951430521],
[51.04643585043994, -114.0692082415949],
[51.045661225557105, -114.06932214141982],
[51.045907290577894, -114.06914372300942],
[51.0460946116025, -114.06918184644789],
[51.045840141392915, -114.0693971680036],
[51.04574051492091, -114.06929040386943],
[51.045597802903025, -114.069439641779],
[51.04630950560272, -114.06922939827352],
[51.04658359955581, -114.06910094765479],
[51.045062981237535, -114.06934626919667],
[51.04642827200508, -114.06932853099767],
[51.04645859384365, -114.06927223287998],
[51.04491009405915, -114.06938197702685],
[51.045162024423895, -114.06915045430895],
[51.044951479373424, -114.06938588591501],
[51.04635320299235, -114.0690992256072],
[51.04609250970501, -114.06912641653663],
[51.04567546703581, -114.06926753967592],
[51.045194291041526, -114.06942554781068],
[51.04568695321445, -114.06929933086211],
[51.04519342215564, -114.06909811465349],
[51.0452277253838, -114.06930778714614],
[51.046532148382575, -114.06927793309114],
[51.04561975547346, -114.06943652125088],
[51.04560596378533, -114.06935883722142],
[51.04600689547791, -114.06929402076078],
[51.044965525013964, -114.0691662081608],
[51.04507740455043, -114.06926368035379],
[51.04641074389775, -114.06914258322705],
[51.04634742860124, -114.0691298517807],
[51.04561683823306, -114.06926519132519],
[51.04655106908159, -114.06935673034825],
[51.04585993585846, -114.06924176816221],
[51.04582832317382, -114.06921552922464],
[51.04493155294905, -114.06931776303342],
[51.04511722896445, -114.06918427579237],
[51.04648789498645, -114.06930905642142],
[51.0463330081317, -114.069323697163],
[51.04523946690684, -114.06909756567865],
[51.04571986128827, -114.06914204466959],
[51.046050920359974, -114.06924862380343],
[51.04505234395438, -114.06929733994963],
[51.0454634147169, -114.06938877411287],
[51.04526192522936, -114.06923540817313],
[51.04561402362053, -114.06933663143691],
[51.04523741678479, -114.06919819671566],
[51.04556087978329, -114.06928371831788],
[51.04616044697719, -114.0693912602567],
[51.04601981827782, -114.06912869243254],
[51.045239051761854, -114.06919992638704],
[51.04565925191445, -114.06927313933977],
[51.04569275537644, -114.06941453832502],
[51.04590289274155, -114.06925411242504],
[51.04633722117736, -114.06943430437322],
[51.04548371897456, -114.06922185974177],
[51.0461756689258, -114.06927066633914],
[51.046200280234935, -114.06910268527459],
[51.045948773049155, -114.06922473229864],
[51.044922031016974, -114.0691566499006],
[51.04500168519232, -114.06925720143602],
[51.045792889112, -114.06914782523673],
[51.04547815637911, -114.06918334195785],
[51.045273624987196, -114.06935507131175],
[51.04525147308883, -114.0691979655243],
[51.04619600672082, -114.0693638167705],
[51.04545106836599, -114.0692419747456],
[51.04597584842397, -114.06923407826173],
[51.04504221908619, -114.0691469428765],
[51.04561123972919, -114.06921296331717],
[51.04498771943865, -114.06912702482649],
[51.045258618469134, -114.06920073449452],
[51.04502513833056, -114.06932938894518],
[51.04605743570279, -114.06931224989081],
[51.04564524368524, -114.06937281928789],
[51.046229711265376, -114.06940558072576],
[51.046429332005665, -114.06942891634672],
[51.04590038965029, -114.06932912472354],
[51.0451103208109, -114.0693878984337],
[51.04552690273258, -114.06931270508903],
[51.04645807864247, -114.06940803985573],
[51.04597104876406, -114.0694098962563],
[51.04557437766565, -114.06923507357034],
[51.046104839836126, -114.06922076795108],
[51.04657347520047, -114.06925056937611],
[51.04490942669556, -114.06941742169735],
[51.04539804368481, -114.06931183760693],
[51.0458020625436, -114.06917685824335],
[51.045665409973175, -114.06924469755445],
[51.04656895042342, -114.0693311282081],
[51.046049841619265, -114.06913648864958],
[51.046222735484015, -114.06932938237821],
[51.04510892083704, -114.06933399181531],
[51.046087347822066, -114.0691863522879],
[51.04488288628077, -114.0693034670645],
[51.04625588052373, -114.0691229555451],
[51.04528218878954, -114.0691698029397],
[51.04517419549356, -114.06941913462971],
[51.044986408307366, -114.06924281205698],
[51.04638999027456, -114.06912870177969],
[51.04597910851427, -114.06936899631202],
[51.045184129884255, -114.0691748768627],
[51.04635016900682, -114.06915664425699],
[51.045459150597885, -114.06924136890146],
[51.04629262663488, -114.06923491228746],
[51.04651097608027, -114.06934126631417],
[51.04525608283231, -114.0692835803247],
[51.04646905159189, -114.06927266467909],
[51.0451642897693, -114.06918546168978],
[51.04523229801216, -114.0694358751274],
[51.04503761369027, -114.0691879859978],
[51.04535851547364, -114.06928422043443],
[51.045956693625754, -114.06919026291476],
[51.0460301241149, -114.06940883990643],
[51.04547076190476, -114.06934097373492],
[51.04614442090765, -114.0693255883398],
[51.04636077407958, -114.06922472672336],
[51.04514385195447, -114.06910302822163],
[51.04592370771643, -114.069262051287],
[51.046048151767394, -114.06918867864191],
[51.04552313238736, -114.06940699508966],
[51.04647058642121, -114.06938009813427],
[51.045954428179165, -114.06913232731267],
[51.04528995030651, -114.0693920430853],
[51.045382835258096, -114.06911764023135],
[51.04641441478214, -114.06920285706636],
[51.04649685360269, -114.06932018046446],
[51.045032802636115, -114.06936241078157],
[51.04611638166738, -114.06913203022616],
[51.046277372561306, -114.06939032623283],
[51.04656337990219, -114.06939829803858],
[51.045801736368915, -114.06935888277395],
[51.046395777714174, -114.06935726732922],
[51.04594810473825, -114.06925191689834],
[51.04638480353121, -114.06917699054085],
[51.045304658287925, -114.0691831915155],
[51.045764910517214, -114.0691276053],
[51.04569447524179, -114.06939712466793],
[51.04586399532015, -114.06937668835646],
[51.04538711206802, -114.06936143157961],
[51.04514266326214, -114.06935825200988],
[51.04526062949984, -114.06916314813803],
[51.04494187916251, -114.0691325268221],
[51.0454345839466, -114.06938866778768],
[51.045351462306314, -114.06923546351885],
[51.04546226339588, -114.06937683807864],
[51.04599053283735, -114.06913392590626],
[51.044922236075486, -114.06923782701398],
[51.04573119774385, -114.06929883593595],
[51.0458031029162, -114.06940938346011],
[51.04494847643336, -114.0691640707783],
[51.045393195720784, -114.06924027998288],
[51.04533070917508, -114.06929370124907],
[51.045899847980344, -114.06941214050335],
[51.04502846572744, -114.06935819951043],
[51.0460367798238, -114.069207519183],
[51.04614327786426, -114.06938153346721],
[51.045103084777416, -114.06927201110513],
[51.04599735579011, -114.06927760413429],
[51.04648928369522, -114.0692973393132],
[51.04618181650117, -114.06910627119676],
[51.04550792031965, -114.06915477680452],
[51.04545185249249, -114.06913025138081],
[51.044977212235, -114.06919392632088],
[51.04520169848496, -114.06943646300749],
[51.0449613429821, -114.0691947945116],
[51.045721217251774, -114.06912692924065],
[51.04629008331312, -114.0693092614656],
[51.046544417520906, -114.06935714180987],
[51.04514356326789, -114.06924346040762],
[51.04489924205852, -114.06941182567112],
[51.04609018194842, -114.06937124653247],
[51.04592351958967, -114.06938333448933],
[51.04490483840049, -114.06915884807142],
[51.04626806093437, -114.06913644569708],
[51.04494889380019, -114.0693099564924],
[51.045089498093084, -114.06916911298558],
[51.04652853481494, -114.06934492722344],
[51.04646161425815, -114.06935177313713],
[51.045649497523954, -114.0693554258492],
[51.04575059386226, -114.06934809321905],
[51.04596643249735, -114.06909876926215],
[51.046140832482266, -114.06917158318954],
[51.046514544545005, -114.06927037494737],
[51.04526069164355, -114.06942328795766],
[51.045955524613376, -114.06918214588468],
[51.04612185543294, -114.06934181217333],
[51.04567720498967, -114.06930728245752],
[51.045643754014094, -114.06926221993129]])

plt.figure(figsize=(10,5))
from sklearn.datasets.samples_generator import make_blobs

X = data

plt.scatter(X[:, 0], X[:, 1], s=50);

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=40)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')


centers = kmeans.cluster_centers_
plt.xlim([51.0445, 51.047])
plt.ylim([-114.069, -114.0695])


plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);

print(centers.tolist())

# POST request
r = requests.post('http://localhost:8080/locationRequest', data = {"centers": centers.tolist()})
print(r.content)
