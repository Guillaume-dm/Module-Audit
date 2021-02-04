# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Adquat_Listing(models.Model):
    _name = 'adquat_audit.listing'
    _description = 'adquat_adquat.adquat_listing'

    l_liste_deux = fields.One2many('ajt_compterenddd', 'liste_deux', string="Lien vers la liste des états.")


class Adquat_Listingg(models.Model):
    _name = 'adquat_audit.listingg'
    _description = 'adquat_adquat.adquat_listingg'

    l_liste_un = fields.One2many('ajt_compterendd', 'liste_un', string="Lien vers la liste des catégories.")


class Adquat_Audit(models.Model): # Classe principale du module
    _name = 'adquat_audit.audit'
    _description = 'adquat_audit.adquat_audit'

    name = fields.Char('🖊️ Titre de l\'audit')
    salarie_id = fields.Many2one('res.users',
                                    ondelete='set null', string="Responsible", index=True)
    date_creation = fields.Date('🏁 Date de début')

    introduction = fields.Text('Ecrire ici') # Permet la possibilité d'écrire une introduction sur plusieurs lignes
    serveurs_virtuels = fields.Boolean('💭 Serveurs virtuels')
    serveurs_reels = fields.Boolean('🏭 Serveurs physiques')
    acces_internet = fields.Image('🌐📶 Accès Internet')
    acces_internet_2 = fields.Char('🌐📶 Accès Internet')
    messagerie = fields.Char('📧 Messagerie')
    prec_meesagerie = fields.Boolean('➕ Ajouter une préconisation')
    hyperviseur = fields.Char('📦 Configuration hyperviseur')
    local = fields.Char('🎛️ Local informatique')
    baie = fields.Char('🔌 Baie informatique')

    prec_parcinfo = fields.Boolean('➕ Ajouter une préconisation')
    prec_parcinfo_text = fields.Char('➕ Ajouter une préconisation')

    pol_windows = fields.Char('')
    antivirus = fields.Char(' ')
    antispam = fields.Char(' ')
    parefeu = fields.Char(' ')
    chiffrage = fields.Char(' ')
    vpn = fields.Char(' ')
    sauvegardes = fields.Char(' ')

    l_serveur_reel = fields.One2many('ajt_serveur_ree', 't_serveur_reel', string=" ")
    l_serveur_virt = fields.One2many('ajt_serveur_vir', 't_serveur_virt', string=" ")
    l_reseau = fields.One2many('ajt_resea', 't_reseau', string=" ")
    l_equipements = fields.One2many('ajt_equipement', 't_equipement', string=" ")
    l_ram = fields.One2many('ajt_parcinf', 'audit', string=" ")
    l_preconisation = fields.One2many('ajt_compterend', 't_preconisation', string=" ")

    def copy(self, default=None): # Appel de la méthode
        default = default or {}
        res = super(Adquat_Audit, self).copy(default)
        res.name = "copie "+res.name
        for line in self.l_serveur_reel:
            line.copy({'t_serveur_reel': res.id})
        for line in self.l_serveur_virt:  # Pour les serveurs virtuels
            line.copy({'t_serveur_virt': res.id})
        for line in self.l_reseau:  # Pour les caractéristiques de réseau
            line.copy({'t_reseau': res.id})
        for line in self.l_equipements:  # Pour les équipements
            line.copy({'t_equipement': res.id})
        for line in self.l_ram:  # Pour les appareils du parc informatique
            line.copy({'audit': res.id})
        for line in self.l_preconisation:  # Pour les préconisations finales
            line.copy({'t_preconisation': res.id})
        return res


class Ajt_Serveur_Reel(models.Model): # Est utilisé uniquement si le booléen des serveurs réels est à true
    _name = 'ajt_serveur_ree'
    _description = "Sert à ajouter les serveurs de type réels."

    t_serveur_reel = fields.Many2one('adquat_audit.audit', string="Serveurs réels")
    ip = fields.Char() # Permet de saisir manuellement l'ip du serveur réel
    nom_serveur = fields.Char() # Permet de saisir manuellement le nom du serveur réel
    marque = fields.Many2one('une_marque', string="🔸 Marque")
    modele_serveur = fields.Many2one('un_modele_serveur', string="⚙ Modèle")
    numero_serie = fields.Char()
    garantie = fields.Many2one('une_garantie', string="🛠️ Garantie")
    role_windows = fields.Many2one('un_role', string="☑ Rôle Windows")
    autre_role = fields.Many2one('un_autre_role', string='✅ Autre(s) rôle(s)')
    processeur = fields.Many2one('un_processeur', string="⚡ Processeur")
    ram2 = fields.Many2one('une_ram', string='♨‍ RAM')
    disque_dur = fields.Many2one('un_disque', string='💽 Disque dur')
    systeme_raid = fields.Many2one('un_systeme_raid', string='💽💽 Carte et système raid')
    os = fields.Many2one('un_os', string='⚙ OS')
    emplacement = fields.Many2one('un_emplacement', string="🔎 Emplacement physique")


class Ajt_Serveur_Virt(models.Model): # Est utilisé uniquement si le booléen des serveurs virtuels est à true
    _name = 'ajt_serveur_vir'
    _description = "Sert à ajouter les serveurs de type virtuels."

    t_serveur_virt = fields.Many2one('adquat_audit.audit', string="☁ Serveurs virtuels")
    ip = fields.Char() # Permet de saisir manuellement l'ip du serveur virtuel
    nom_serveur = fields.Char() # Permet de saisir manuellement le nom du serveur virtuel
    marque = fields.Many2one('une_marque', string="🔸 Marque")
    role_windows = fields.Many2one('un_role', string="☑ Rôle Windows")
    autre_role = fields.Many2one('un_autre_role', string='✅ Un autre rôle')
    processeur = fields.Many2one('un_processeur', string="⚡ Processeur")
    ram2 = fields.Many2one('une_ram', string='♨‍ RAM')
    disque_dur = fields.Many2one('un_disque', string='💽 Disque dur')
    os = fields.Many2one('un_os', string='⚙ OS')


class Ajt_Reseau(models.Model):
    _name = 'ajt_resea'
    _description = "Sert à renseigné le réseau."

    t_reseau = fields.Many2one('adquat_audit.audit', string="Réseau")
    site = fields.Many2one('un_site', string="📍 Site")
    plage_ip = fields.Char() # Permet de saisir manuellement la plage d'ip du réseau
    masque = fields.Char() # Permet de saisir manuellement le masque du sous-réseau
    routeur = fields.Char()
    dns = fields.Char() # Permet de saisir manuellement le DNS


class Ajt_Equipements(models.Model):
    _name = "ajt_equipement"
    _description = "Sert à ajouter un équipement."

    t_equipement = fields.Many2one('adquat.audit.audit', string="Equipements")
    site = fields.Many2one('un_site', string="📍 Site")
    nom_description = fields.Many2one('un_nom_description', string="❓ Nom/description")
    marque = fields.Many2one('une_marque', string="🔸 Marque")
    modele_equipement = fields.Many2one('un_modele_equipement', string="⚙ Modèle")
    fonction = fields.Many2one('une_fonction', string="✅ Fonction")
    emplacement = fields.Many2one('un_emplacement', string="🔎 Emplacement physique")


class Ajt_ParcInfo(models.Model):
    _name = 'ajt_parcinf'
    _description = "RAS"

    audit = fields.Many2one('adquat_audit.audit', string="🖥️ Audit")
    username = fields.Char() # Permet de saisir l'username de l'utilisateur de l'ordinateur
    modele = fields.Many2one('un_modele', string="Modèle")
    systeme = fields.Many2one('un_systeme_e', string="🖥️ Systeme d'exploitation")
    processeur = fields.Many2one('un_processeur', string="⚡ Processeur")
    ram2 = fields.Many2one('une_ram', string="♨‍ RAM")
    type_sto = fields.Many2one('un_type_sto', string='Type(s) de stockage')
    office = fields.Many2one('un_office', string="⌨ Version d'office")
    commentaires = fields.Text() # Permet de saisir des remarques annexes


class Modele(models.Model):
    _name = 'un_modele'
    _description = "Sert à définir le modèle de l'appareil."

    name = fields.Char()


class Modele_Serveur(models.Model):
    _name = 'un_modele_serveur'
    _description = "Sert à définir le modèle du serveur réel."

    name = fields.Char()


class Modele_Equipements(models.Model):
    _name = 'un_modele_equipement'
    _description = "Sert à définir le modèle de l'équipement."

    name = fields.Char()


class Systeme_E(models.Model):
    _name = 'un_systeme_e'
    _description = "Sert à définir le système d'exploitation."

    name = fields.Char()


class Processeur(models.Model):
    _name = 'un_processeur'
    _description = "Sert à définir le processeur."

    name = fields.Char()


class Type_Sto(models.Model):
    _name = 'un_type_sto'
    _description = "Sert à définir le type de stockage."

    name = fields.Char()


class Ajt_Compterendu(models.Model):
    _name = 'ajt_compterend'
    _description = "Sert à ajouter une préconisation finale."

    t_preconisation = fields.Many2one('adquat_audit.audit', string="⚠ Préconisation")
    liste_un = fields.Many2one('une_liste_un', string="Liste de préconisation")
    preconisation = fields.Text() # Permet de saisir une description de préconisation à la main
    liste_deux = fields.Many2one('une_liste_deux', string="🚦 Liste des états de préconisation")


class Ajt_Compterendu2(models.Model):
    _name = 'ajt_compterendd'
    _description = "Sert à voir les catégories des préconisations finales."

    liste_un = fields.Many2one('une_liste_un', string="🚦 Liste des catégories")


class Ajt_Compterendu3(models.Model):
    _name = 'ajt_compterenddd'
    _description = "Sert à voir les états des préconisations finales."

    liste_deux = fields.Many2one('une_liste_deux', string="🚦 Liste des états de préconisation")


class Site(models.Model):
    _name = "un_site"
    _description = "Sert à définir le lieu du réseau."

    name = fields.Char()


class Marque(models.Model):
    _name = "une_marque"
    _description = "Sert à définir la marque du serveur."

    name = fields.Char()


class Garantie(models.Model):
    _name = "une_garantie"
    _description = "Sert à définir la durée de garantie pour un serveur réeL."

    name = fields.Char()


class Role_Windows(models.Model):
    _name = "un_role"
    _description = "Sert à définir les rôles d'un serveur donné."

    name = fields.Char()


class Autre_Role(models.Model):
    _name = "un_autre_role"
    _description = "Sert à définir un autre rôle pour un serveur."

    name = fields.Char()


class Disque_Dur(models.Model):
    _name = "un_disque"
    _description = "Sert à définir le type, la quantité et le nombre de disque dur d'un appareil donné."

    name = fields.Char()


class Systeme_Raid(models.Model):
    _name = "un_systeme_raid"
    _description = "Sert à définir le système raid d'un serveur réel."

    name = fields.Char()


class Os(models.Model):
    _name = "un_os"
    _description = "Sert à définir l'OS d'un serveur."

    name = fields.Char()


class Ram(models.Model):
    _name = "une_ram"
    _description = "Sert à définir la valeur de la RAM d'un appareil."

    name = fields.Char()


class NomDescription(models.Model):
    _name = "un_nom_description"
    _description = "Sert à définir le nom et/ou la description d'un appareil."

    name = fields.Char()


class Emplacements(models.Model):
    _name = "un_emplacement"
    _description = "Sert à définir l'emplacement physique d'un appareil."

    name = fields.Char()


class Fonction(models.Model):
    _name = "une_fonction"
    _description = "Sert à définir la oun les fonctions d'un appareil."

    name = fields.Char()


class Liste_Préconisation(models.Model):
    _name = "une_liste_un"
    _description = "Sert à afficher la liste des différentes préconsisations possibles."

    name = fields.Char("🆕 Ajouter/modifier un type de préconisation")


class Liste_Etats(models.Model):
    _name = "une_liste_deux"
    _description = "Permet automatiquement l'affichage d'état en passtille par couleur, " \
                   "sans avoir à les implémenter manuellement."

    name = fields.Char("🆕 Ajouter/modifier un niveau d'urgence")


class Office(models.Model):
    _name = "un_office"
    _description = "Sert à définir la version d'Office pour un ordinateur du parc informatique donné."

    name = fields.Char()


