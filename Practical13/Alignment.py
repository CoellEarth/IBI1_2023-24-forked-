#import the modules to be used, and use blosum to read the BLOSUM62 matrix
import re
import blosum as bl
matrix = bl.BLOSUM(62)

#input the sequences to be checked
human = 'METTPLNSQKQLSACEDGEDCQENGVLQKVVPTPGDKVESGQISNGYSAVPSPGAGDDTRHSIPATTTTLVAELHQGERETWGKKVDFLLSVIGYAVDLGNVWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIMAWALYYLISSFTDQLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGGISWQLALCIMLIFTVIYFSIWKGVKTSGKVVWVTATFPYIILSVLLVRGATLPGAWRGVLFYLKPNWQKLLETGVWIDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHVWAKRRERFVLAVVITCFFGSLVTLTFGGAYVVKLLEEYATGPAVLTVALIEAVAVSWFYGITQFCRDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPYWSIILGYCIGTSSFICIPTYIAYRLIITPGTFKERIIKSITPETPTEIPCGDIRLNAV'
mouse = 'METTPLNSQKVLSECKDKEDCQENGVLQKGVPTPADKAGPGQISNGYSAVPSTSAGDEAPHSTPAATTTLVAEIHQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWKKICPIFKGIGYAICIIAFYIASYYNTIIAWALYYLISSFTDQLPWTSCKNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQSKGLQDLGTISWQLALCIMLIFTIIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLPGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCILGSLLTLTSGGAYVVTLLEEYATGPAVLTVALIEAVVVSWFYGITQFCSDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIILGYCIGTSSVICIPIYIIYRLISTPGTLKERIIKSITPETPTEIPCGDIRMNAV'
rat = 'METTPLNSQKVLSECKDREDCQENGVLQKGVPTTADRAEPSQISNGYSAVPSTSAGDEASHSIPAATTTLVAEIRQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIIAWALYYLISSLTDRLPWTSCTNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQSKGLQDLGTISWQLTLCIVLIFTVIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLPGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCVLGSLLTLTSGGAYVVTLLEEYATGPAVLTVALIEAVAVSWFYGITQFCSDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIVLGYCIGMSSVICIPTYIIYRLISTPGTLKERIIKSITPETPTEIPCGDIRMNAV'

#create a functioon for alignment_score and identical_count for the two sequences
def Similarity_assessment(seq1_name,seq1,seq2_name,seq2):
    #initialize the values
    alignment_score = 0
    identical_count = 0
    #create loops for each amino acid in the seq1
    for i in range(len(seq1)):
        #if the amino acid is the same, +1 to identical_count
        if seq1[i] == seq2[i]:
            identical_count += 1
        #for each pair of amino acid, add the corresponding alignment_score
        alignment_score += matrix[seq1[i]][seq2[i]]
    percentage_identity = (identical_count / len(human)) * 100
    #return the result of the test
    return f' the identity percentage is {percentage_identity}% between {seq1_name} and {seq2_name} and the alignment_score is {alignment_score} between {seq1_name} and {seq2_name}'

print(Similarity_assessment('Human',human,'Mouse',mouse))
print(Similarity_assessment('Human',human,'Rat',rat))
print(Similarity_assessment('Rat',rat,'Mouse',mouse))
