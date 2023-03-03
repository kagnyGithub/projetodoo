from odoo import models, fields
class AgenceVehicule(models.Model):
    _name = 'agence.vehicule'
    marque_id = fields.Many2one(
        'agence.marque',
        ondelete='set null',
        context={},
        domain=[],
        string='Marque')
    
    modele = fields.Char('Modèle', required=True)
    date_achat = fields.Date('Date d Achat')
    chaffeur_ids = fields.Many2many(
        'res.partner',
        string='Chaffeurs'
    )
    matricule = fields.Char('Matricule', required=True)
    notes = fields.Text('Notes Internes',
                        translate=True)  # Pour permettre la traduction du champ
    state = fields.Selection(
        [('new', 'Nouveau'),
         ('fonctional', 'Fonctionnel'),
         ('on_repair', 'En Réparation'),
         ('declassed', 'Déclassé')],
        'Etat', default="new")
    description = fields.Html('Description')
    image_v = fields.Binary('Image de Véhicule')
    active = fields.Boolean('Active', default=True)
    veh_service = fields.Boolean('Véhicule de Service ?', default=False)
    nb_places = fields.Integer('Nombre de palces', default=5)
    dern_kilometrage = fields.Float('Dernier Kilométrage',
                                    digits=(14, 2),  # spcifier la précision
                                    groups='base.group_user',  # Le groupe (droits d'accès à ce champ)
                                    states={'on_repair': [('readonly', True)],
                                            'declassed': [('invisible', True)]
                                            },
                                    # mode lecture seul si l'état=En Réparation
                                    # invisible seul si l'état=Déclassé
                                    help='Mettez ici le Dernier relevé kilomètrique'
                                    # c'est le message d'aide de ce champ à l'utilisateur
                                    )
    prix_achat_v = fields.Float('Prix d’achat')
    category_id = fields.Many2one('agence.categorie.vehicule', string='Catégorie')
    currency_id = fields.Many2one('res.currency',
                                  string='Symbole Monétaire')  # On sauvegarde le symblode dans ce varibale
    prix_vente_v = fields.Monetary('Pix de Vente',
                                   digits='Prix Véhicule',  # Précision configurable par le end user
                                   currency_field='currency_id',  # ce champ est optionnel mais recommandé )

                                   )

    _sql_constraints = [
        ('mat_uniq', 'UNIQUE (matricule)',
         'Les Matricules doivent être uniques !'
         ),
        ('nb_place_positif', 'CHECK (nb_places >=2)',
         'Le nombre de place doit être suppérieur ou égale à 2 !'
         )
    ]
