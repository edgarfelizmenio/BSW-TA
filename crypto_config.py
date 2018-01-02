from charm.core.engine.util import objectToBytes,bytesToObject

from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc 

group_object = PairingGroup('SS512')
cpabe = CPabe_BSW07(group_object)
hybrid_abe = HybridABEnc(cpabe, group_object)

(pk, mk) = hybrid_abe.setup()
pk_string = str(objectToBytes(pk, group_object), 'utf-8')
mk_string = str(objectToBytes(mk, group_object), 'utf-8')