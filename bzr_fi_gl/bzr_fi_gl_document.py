# -*- coding: utf-8 -*-

from openrp.osv import fields, osv
#会计凭证   fi.doc
#会计凭证行 fi.doc.line
#辅助核算行 fi.doc.line.cost

class fi_doc_line_cost(osv.osv):
    _name = 'fi.doc'
    _description = "会计凭证"
    _columns = {
#凭证日期
        'date':
#会计期间
        'period_id':fields.many2one('fi.period','期间',required=True,
        states={'posted':[('readonly',True)]},help='过账后不可修改'),        
#凭证字
        'type_id':fields.many2one('fi.doc.type','凭证字',required=True,
        help='可在配置中自定义'),
#凭证号
        'number':fields.char('凭证编号',size=64,
        help='由系统自动生成，结帐前可重排'),
#附件张数
        'ref_count':fields.integer('附件张数',help='凭证后附原始凭证的页数'),
#凭证行
        'line_ids':fields.one2many('fi.doc.line','doc_id','凭证行',
        states={'posted':[('readonly',True)]},help='过账后不可修改'),
#状态
#TODO:此处改成从ir_states表读取
# select key text from ir_states where object='fi.doc'
        'state':fields.selection([('draft','不平衡')],'状态',required=True, 
        readonly=True,help='控制会计凭证工作流'),
#制单
        'create_uid':fields.many2one('res.users','制单',
        help='凭证制单人'),
#审核
        'approve_uid':fields.many2one('res.users','审核',
        help='凭证审核人'),
#登账
        'post_uid':fields.many2one('res.users','记账',
        help='凭证登帐人'),
    }


class fi_doc_line(osv.osv):
    _name = 'fi.doc.line'
    _description = "会计凭证行"
    _columns = {
#会计凭证
        'doc_id':fields.many2one('fi.doc','会计凭证',required=True)
#摘要
        'text':fields.char('摘要',size=64,help='凭证行的摘要'),
#会计科目
        'acc_id':fields.many2one('fi.acc','会计科目',help='只能选择末级科目'),
#借方
#TODO 这里这个'Account'能否使用当前class的name？
        'debit': fields.float('借方',help='以公司本位币计的金额', 
        ,digits_compute=dp.get_precision('Account')),
#贷方
        'credit': fields.float('贷方',help='以公司本位币计的金额',
        digits_compute=dp.get_precision('Account')),        

#辅助核算行
        'cost_ids':fields.one2many('fi.doc.line.cost','line_id','辅助核算行'),   
    }


class fi_doc_line_cost(osv.osv):
    _name = 'fi.doc.line.cost'
    _description = "辅助核算行"
    _columns = {
#凭证行编号
        'line_id':fields.many2one('fi.doc.line','凭证行'),
#辅助核算项目
        'co_obj':fields.reference('辅助核算项目'),
#金额
        'amount':
#产品相关
#数量
        ''
#单位
        ''
#业务伙伴相关
#到期日            
    }