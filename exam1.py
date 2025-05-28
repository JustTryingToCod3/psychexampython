from ast import While
from pickle import TRUE
class Question:
    def __init__(self, prompt, correct_answer):
        self.prompt = prompt
        self.correct_answer = correct_answer

    def check_answer(self, user_input):
        return user_input.strip().lower() == self.correct_answer.lower()

def run_exam(questions):
    while True:
        your_score = 0
        total_score = len(questions)

        for q in questions:
            answer = input(q.prompt + "\nYour answer: ")
            if q.check_answer(answer):
                print("✅ Correct")
                your_score += 1
            elif answer.strip().lower() == "0":
              break
            else:
                print("❌ Incorrect")
                print(f"The correct answer was: {q.correct_answer.upper()}")

        percentage = (your_score / total_score) * 100
        grade = handle_grades(percentage)

        print(" ")
        print(f"\nYour Score: {your_score}/{total_score} ({percentage:.2f}%)")
        print(f"Your Letter Grade: {grade}")
        print(" ")

        # Ask to retake the quiz
        again = input("\nWould you like to retake the exam or continue? Press y to retake and n to continue? (y/n): ").strip().lower()
        print(" ")
        if again != "y":
            print("Thank you for taking the exam! Good luck with your studies 😊")
            break

def handle_grades(percentage):
        if percentage >= 90: return "A, you earned a Diamond"
        elif percentage >= 80: return "B you found a four leaf clover"
        elif percentage >= 70: return "C you tripped over a rock, don't worry, no one saw"
        elif percentage >= 60: return "D congrats on showing up.. at least..."
        return "F... no words here.... Start over"

psy1 = [
        Question("What is Major Depressive Disorder (MDD)?\na. A mood disorder with alternating manic and depressive episodes\nb. A mood disorder marked by persistent sadness and loss of interest", "b"),
        Question("What is Bipolar Disorder?\na. A disorder marked by mood swings between depression and mania\nb. A persistent low mood without mania", "a"),
        Question("What is a key difference between depression and bipolar disorder?\na. Bipolar includes manic/hypomanic episodes; depression does not\nb. Depression includes mood elevation; bipolar does not", "a"),
        Question("What is the typical duration for a major depressive episode?\na. 2 weeks or more\nb. 2 months or more", "a"),
        Question("What characterizes persistent depressive disorder?\na. Chronic depression lasting at least 2 years\nb. Cyclical mood changes over weeks", "a"),
        Question("What is a manic episode?\na. A state of low energy and fatigue\nb. A period of elevated or irritable mood with increased activity", "b"),
        Question("How is Bipolar I Disorder diagnosed?\na. At least one manic episode\nb. At least one hypomanic episode with no mania", "a"),
        Question("How is Bipolar II Disorder diagnosed?\na. One major depressive episode only\nb. Hypomania and major depressive episodes without full mania", "b"),
        Question("What is Cyclothymic Disorder?\na. Chronic mild mood swings without full mania or depression\nb. Alternating full manic and depressive episodes", "a"),
        Question("Which theory emphasizes genetic and neurotransmitter factors in mood disorders?\na. Biological Theory\nb. Psychodynamic Theory", "a"),
 ]
psy2 = [
        Question("Which neurotransmitters are often low in depression?\na. Serotonin and norepinephrine\nb. Acetylcholine and GABA", "a"),
        Question("What brain areas are involved in mood regulation?\na. Prefrontal cortex, amygdala, hippocampus\nb. Brain stem, cerebellum, occipital lobe", "a"),
        Question("What is the role of cortisol in depression?\na. Reduced cortisol leads to depression\nb. Elevated cortisol is linked to depressive symptoms", "b"),
        Question("What is the role of lithium in bipolar disorder?\na. Mood stabilizer that prevents manic/depressive episodes\nb. Antidepressant that boosts serotonin", "a"),
        Question("Which therapy helps regulate daily routines in bipolar treatment?\na. Interpersonal and Social Rhythm Therapy (IPSRT)\nb. Exposure Therapy", "a"),
        Question("What is the focus of Cognitive Behavioral Therapy (CBT)?\na. Unconscious conflicts from childhood\nb. Identifying and changing negative thought patterns", "b"),
        Question("What is Beck’s Cognitive Triad?\na. Positive thoughts about self, world, and future\nb. Negative thoughts about self, world, and future", "b"),
        Question("What is the learned helplessness theory?\na. Belief that actions can influence outcomes\nb. Perception that efforts have no impact, leading to depression", "b"),
        Question("Which theory explains depression through repressed loss and unresolved grief?\na. Psychodynamic theory\nb. Behavioral theory", "a"),
        Question("Which treatment method is most commonly used in psychodynamic therapy?\na. Free association and interpretation\nb. Behavioral activation scheduling", "a"),
        Question("What does behavioral theory suggest causes depression?\na. Repressed unconscious drives\nb. Lack of positive reinforcement and learned behaviors", "b"),
        Question("What is behavioral activation?\na. Increasing avoidance behaviors\nb. Encouraging engagement in rewarding activities", "b"),
        Question("What is the goal of CBT in bipolar disorder?\na. Eliminate manic episodes\nb. Manage symptoms and reduce cognitive distortions", "b"),
        Question("What are SSRIs used for?\na. Increasing serotonin activity to treat depression\nb. Decreasing serotonin to stabilize mood", "a"),
        Question("What is Electroconvulsive Therapy (ECT) used for?\na. Mild depression\nb. Severe or treatment-resistant depression", "b"),
]
psy3 = [
        Question("What does IPT (Interpersonal Therapy) focus on?\na. Unconscious motivation\nb. Improving communication and resolving social conflicts", "b"),
        Question("What does the sociocultural model emphasize?\na. Neurochemical imbalances\nb. Impact of social environment, relationships, and culture", "b"),
        Question("Which population is twice as likely to experience depression?\na. Men\nb. Women", "b"),
        Question("How does social support affect depression risk?\na. Lack of support increases depression risk\nb. Support has no effect on mood", "a"),
        Question("How does culture affect how depression is expressed?\na. All cultures express depression the same\nb. Some cultures show physical symptoms more than emotional ones", "b"),
        Question("What is rumination?\na. Ignoring negative thoughts\nb. Repetitive focus on negative emotions and thoughts", "b"),
        Question("How do MAO inhibitors treat depression?\na. Increase serotonin/norepinephrine by blocking enzyme breakdown\nb. Block dopamine receptors", "a"),
        Question("What is a risk when using antidepressants in bipolar disorder?\na. They can trigger manic episodes\nb. They stabilize mood effectively", "a"),
        Question("What are mood stabilizers?\na. Medications for anxiety\nb. Drugs that prevent mood swings in bipolar disorder", "b"),
        Question("What is the purpose of family-focused therapy in bipolar disorder?\na. Treat psychotic symptoms\nb. Improve communication and reduce relapse", "b"),
        Question("What is the developmental psychopathology perspective?\na. Focuses on short-term symptoms only\nb. Integrates biology, psychology, and environment over time", "b"),
        Question("What is the attribution-helplessness theory?\na. Belief that negative outcomes are random\nb. Internal, global, and stable attributions lead to hopelessness", "b"),
        Question("Which therapy emphasizes mindfulness and acceptance of thoughts?\na. CBT\nb. ACT (Acceptance and Commitment Therapy)", "b"),
        Question("What type of disorder is premenstrual dysphoric disorder?\na. A type of bipolar disorder\nb. A depressive disorder tied to the menstrual cycle", "b"),
        Question("What is a core feature of DMDD (Disruptive Mood Dysregulation Disorder)?\na. Mood stability\nb. Severe temper outbursts and irritability in children", "b"),
]
psy4 = [        Question("Which theory says depression arises from unmet childhood needs?\na. Cognitive theory\nb. Psychodynamic theory", "b"),
        Question("Which antidepressant class selectively increases serotonin?\na. SSRIs\nb. MAOIs", "a"),
        Question("Which type of therapy combines behavioral and cognitive techniques?\na. Psychodynamic therapy\nb. Cognitive Behavioral Therapy (CBT)", "b"),
        Question("What is a hypomanic episode?\na. A milder form of mania\nb. A depressive episode with psychotic features", "a"),
        Question("Which therapy focuses on adjusting social rhythms and sleep cycles?\na. CBT\nb. IPSRT", "b"),
        Question("What is one goal of psychodynamic therapy for depression?\na. Improve daily activity planning\nb. Bring unconscious conflicts to awareness", "b"),
        Question("What does the behavioral model suggest to reduce depressive symptoms?\na. Increase punishment to reduce negative behavior\nb. Increase positive reinforcement and engagement", "b"),
        Question("What treatment is most effective for mild-to-moderate depression?\na. Medication only\nb. Psychotherapy or a combination with medication", "b"),
        Question("Which theory explains mood disorders as interactions between stress and genetic vulnerability?\na. Stress-diathesis model\nb. Attribution model", "a"),
        Question("How is suicide defined in abnormal psychology?\na. An unintentional self-inflicted injury\nb. A self-inflicted, intentional act resulting in death", "b"),
        Question("What is suicidal ideation?\na. Thoughts about ending one’s life\nb. A completed suicide attempt", "a"),
        Question("Which gender has higher rates of completed suicide?\na. Males\nb. Females", "a"),
        Question("Which gender is more likely to attempt suicide?\na. Males\nb. Females", "b"),
        Question("Suicide is considered:\na. A mental disorder in DSM-5\nb. A public health concern but not classified as a mental disorder", "b"),
]
psy5 = [        Question("What is a subintentional death?\na. An accidental overdose\nb. A covert, indirect, or unconscious form of self-harm leading to death", "b"),
        Question("What is nonsuicidal self-injury (NSSI)?\na. Intentional self-harm without intent to die\nb. A suicidal gesture with lethal intent", "a"),
        Question("What is retrospective analysis in suicide research?\na. Studying genetic data from family trees\nb. Psychological autopsy using post-death information", "b"),
        Question("Which of the following is a limitation in suicide data collection?\na. Accurate self-reports\nb. Underreporting due to stigma or misclassification", "b"),
        Question("What percentage of people who attempt suicide are legally intoxicated?\na. One-fourth\nb. Half", "a"),
        Question("Which mood/thought pattern is strongly associated with suicide risk?\na. Hopelessness\nb. Positive reframing", "a"),
        Question("Dichotomous thinking refers to:\na. Seeing life as full of options\nb. Black-and-white, all-or-nothing thinking", "b"),
        Question("What is the most common mental disorder among suicide attempters?\na. Schizophrenia\nb. Depression", "b"),
        Question("What is the ‘contagion effect’ in suicide?\na. A chemical imbalance in neurotransmitters\nb. A rise in suicide following exposure to others’ suicidal behavior", "b"),
        Question("Which theory suggests suicide stems from repressed anger turned inward?\na. Psychodynamic Theory\nb. Behavioral Theory", "a"),
        Question("According to Freud, suicide may result from:\na. Excessive serotonin activity\nb. Introjection of a lost person", "b"),
        Question("Durkheim’s ‘Egoistic suicide’ refers to:\na. A person closely tied to social groups\nb. A person with weak social bonds", "b"),
        Question("Durkheim’s ‘Altruistic suicide’ is committed by:\na. A socially isolated person\nb. A person who sacrifices for society or group", "b"),
        Question("What is perceived burdensomeness in Joiner’s Interpersonal-Psychological Theory?\na. The belief one is a burden to others\nb. Feeling overly independent", "a"),
        Question("Thwarted belongingness refers to:\na. A sense of community\nb. Social disconnection and isolation", "b"),
]
psy6 = [
        Question("What increases ‘acquired capability’ for suicide?\na. Long-term therapy\nb. Repeated exposure to painful or provocative experiences", "b"),
        Question("Biological factors in suicide include:\na. High serotonin levels\nb. Low serotonin and genetic vulnerability", "b"),
        Question("Which age group in the U.S. has the highest rate of completed suicide?\na. Elderly adults\nb. Teenagers", "a"),
        Question("Which ethnic group in the U.S. shows the highest suicide rates among teens?\na. American Indians\nb. Asian Americans", "a"),
        Question("What is a primary goal of treatment after a suicide attempt?\na. Terminate all therapy\nb. Keep the person alive and reduce psychological pain", "b"),
        Question("Which therapy is especially effective in reducing suicidal behavior in individuals with emotion regulation issues?\na. Dialectical Behavior Therapy (DBT)\nb. Exposure Therapy", "a"),
        Question("Which therapy targets cognitive distortions linked to suicide risk?\na. CBT (Cognitive Behavioral Therapy)\nb. Psychoanalysis", "a"),
        Question("Which of the following is a protective factor against suicide?\na. Social isolation\nb. Strong social support", "b"),
        Question("What role do religious beliefs often play in suicide prevention?\na. No influence at all\nb. Act as a protective cultural factor", "b"),
        Question("Which is an example of a warning sign of suicide?\na. Giving away personal belongings\nb. Joining a new club", "a"),
        Question("What does safety planning involve?\na. Discussing philosophy of ethics\nb. Creating personalized strategies to reduce suicide risk during crisis", "b"),
        Question("Crisis intervention typically includes:\na. Long-term psychoanalytic therapy\nb. Establishing safety and connecting to immediate resources", "b"),
        Question("Which population has the highest suicide rate globally?\na. Adolescents\nb. Elderly", "b"),
        Question("Which is a common behavioral warning sign?\na. Sudden improvement in mood after depression\nb. Increased interest in socializing", "a"),
        Question("What is a common verbal cue associated with suicide risk?\na. Expressing hope for recovery\nb. Talking about being a burden or wanting to die", "b"),
]
psy7 = [
        Question("Which social-environmental factor increases suicide risk?\na. Close family ties\nb. Relationship conflict or isolation", "b"),
        Question("Which factor is most closely linked to adolescent suicide?\na. Better academic performance\nb. Stress, bullying, or identity struggles", "b"),
        Question("What is a major component of community-based suicide prevention?\na. Restricting access to mental health services\nb. Public education and reducing stigma", "b"),
        Question("What should responsible media reporting on suicide avoid?\na. Detailed descriptions of methods\nb. Promoting support resources", "a"),
        Question("What is a common intervention for suicidal teens?\na. Group therapy, family involvement, and CBT\nb. Immediate hospitalization followed by isolation", "a"),
        Question("Which suicide assessment method involves postmortem analysis?\na. Retrospective analysis\nb. Behavioral observation", "a"),
        Question("What makes studying suicide difficult in research?\na. High incidence rates\nb. Low base rate and ethical constraints", "b"),
        Question("What ethical dilemma often arises in suicide treatment?\na. Whether to provide medication\nb. Balancing autonomy with safety", "b"),
        Question("What is the diathesis-stress model in suicide?\na. High stress alone causes suicide\nb. Genetic vulnerability + stress increases suicide risk", "b"),
        Question("What is one limitation of retrospective studies on suicide?\na. Complete accuracy\nb. Potential bias and incomplete data", "b"),
        Question("What is a suicide attempt?\na. An unintentional act of self-harm\nb. A self-harm act with intent to die but does not result in death", "b"),
        Question("Which of the following best describes a completed suicide?\na. Any self-harm behavior\nb. A suicide attempt that results in death", "b"),
        Question("Cognitive theorists emphasize what in understanding suicide?\na. External rewards\nb. Hopelessness and cognitive distortions", "b"),
        Question("Which model combines psychological, biological, and environmental causes of suicide?\na. Biopsychosocial model\nb. Humanistic model", "a"),
        Question("Which term refers to repeatedly thinking about dying or death?\na. Rumination\nb. Suicidal ideation", "b"),
]
psy8 = [
        Question("What is a factitious disorder?\na. Physical symptoms intentionally produced without external reward\nb. Physical symptoms arising from an identifiable medical condition", "a"),
        Question("What is Munchausen syndrome by proxy?\na. Creating symptoms in oneself for attention\nb. Creating symptoms in another person to present them as ill", "b"),
        Question("Which of the following is commonly linked to factitious disorder?\na. Employment in medical settings\nb. Strong social support and family bonds", "a"),
        Question("Are factitious disorders well understood with effective treatment plans?\na. Yes\nb. No", "b"),
        Question("What is conversion disorder characterized by?\na. Symptoms consistent with known medical conditions\nb. Neurological-like symptoms inconsistent with medical disease", "b"),
        Question("In conversion disorder, symptoms are:\na. Consciously produced for external rewards\nb. Unconsciously produced without apparent medical cause", "b"),
        Question("Which disorder involves one or more distressing physical symptoms with excessive thoughts and behaviors?\na. Conversion disorder\nb. Somatic symptom disorder", "b"),
        Question("Which of the following typically lasts longer and includes a broader set of symptoms?\na. Somatic symptom disorder\nb. Conversion disorder", "a"),
        Question("How is the focus different in somatic symptom disorder vs. conversion disorder?\na. Somatic: worry about health implications; Conversion: loss of function or sensation\nb. Somatic: sensory deficits; Conversion: obsessive thought patterns", "a"),
        Question("Which example best illustrates conversion disorder?\na. Glove anesthesia (numbness of entire hand)\nb. Worry about mild headache signaling brain cancer", "a"),
        Question("What is a common feature of both somatic and conversion disorders?\na. Clear physical causes\nb. Psychological factors contributing to physical symptoms", "b"),
        Question("Which model suggests physical symptoms express unconscious emotional conflict?\na. Cognitive-behavioral model\nb. Psychodynamic model", "b"),
]
psy9 = [
        Question("What is primary gain in the psychodynamic view?\na. Attention from others\nb. Avoiding internal conflict by converting it to a physical symptom", "b"),
        Question("What is secondary gain in the psychodynamic model?\na. Gaining external benefits like attention or relief from responsibilities\nb. Blocking unconscious conflicts", "a"),
        Question("What do contemporary psychodynamic theorists believe?\na. Physical symptoms are fully conscious acts\nb. Unconscious childhood conflicts cause anxiety expressed through physical symptoms", "b"),
        Question("Which theory focuses on somatic vigilance and reinforcement?\na. Behavioral/Cognitive model\nb. Humanistic model", "a"),
        Question("In the cognitive-behavioral view, what can maintain somatic symptoms?\na. Insight therapy\nb. Rewards for the sick role and poor communication skills", "b"),
        Question("According to the multicultural view:\na. All cultures equally suppress somatic complaints\nb. Some cultures express distress physically rather than emotionally", "b"),
        Question("Which is a common treatment approach for conversion and somatic symptom disorders?\na. Surgery and hospitalization\nb. Insight therapy, exposure, and cognitive restructuring", "b"),
        Question("What is illness anxiety disorder?\na. Focused on having or acquiring illness with little or no actual symptoms\nb. Focused on multiple real physical symptoms", "a"),
        Question("How long must symptoms last to meet criteria for somatic symptom disorder or illness anxiety disorder?\na. At least 6 months\nb. At least 6 weeks", "a"),
        Question("Which disorder is similar in treatment to OCD and responds to CBT and SSRIs?\na. Illness anxiety disorder\nb. Conversion disorder", "a"),
        Question("What is psychophysiological disorder?\na. Physical illness caused entirely by psychological factors\nb. Physical illness affected by psychological factors like stress", "b"),
        Question("Which of the following is NOT a psychophysiological disorder?\na. Asthma\nb. Conversion disorder", "b"),
        Question("What is the main biological factor in psychophysiological disorders?\na. Defects in the autonomic nervous system\nb. Structural brain damage", "a"),
        Question("Which personality type is more prone to psychophysiological disorders?\na. Type A\nb. Type B", "a"),
        Question("How does stress affect the immune system?\na. Enhances immune response\nb. Weakens immune functioning by slowing lymphocyte activity", "b"),
]
psy10 = [
        Question("Which hormone is associated with immune suppression during stress?\na. Cortisol\nb. Insulin", "a"),
        Question("What does psychoneuroimmunology study?\na. Relationship between genetics and diet\nb. Effects of stress on immune function and health", "b"),
        Question("Which treatment approach involves EMG and relaxation training?\na. Psychodynamic therapy\nb. Behavioral medicine techniques", "b"),
        Question("Which of the following best describes somatic symptom disorder?\na. One or more real physical symptoms with excessive health-related thoughts and behaviors\nb. A conscious effort to deceive others for gain", "a"),
        Question("In somatic symptom disorder, the physical symptom is:\na. Always medically explained\nb. Sometimes real but medically unexplainable", "b"),
        Question("What is a somatization pattern?\na. Repeated doctor visits with changing, unexplained symptoms\nb. A one-time isolated complaint", "a"),
        Question("Which disorder involves seeking repeated medical care for unexplained symptoms across multiple providers?\na. Conversion disorder\nb. Somatic symptom disorder with somatization pattern", "b"),
        Question("What is glove anesthesia?\na. Loss of sensation matching anatomical nerve distribution\nb. Loss of sensation inconsistent with anatomy", "b"),
        Question("Which disorder often presents with neurological symptoms without neurological disease?\na. Illness anxiety disorder\nb. Conversion disorder", "b"),
        Question("Which disorder includes significant anxiety about developing a serious illness despite few or no symptoms?\na. Somatic symptom disorder\nb. Illness anxiety disorder", "b"),
        Question("How does conversion disorder typically present?\na. Physical symptoms that match a medical explanation\nb. Symptoms like paralysis, blindness, or seizures without medical cause", "b"),
        Question("Which psychological model emphasizes symptom reward and modeling in somatic disorders?\na. Behavioral model\nb. Biological model", "a"),
        Question("Which theory views physical symptoms as a means of expressing internal conflict?\na. Sociocultural model\nb. Psychodynamic model", "b"),
]
psy11 = [
        Question("Which therapy teaches patients to reinterpret their bodily symptoms?\na. Exposure therapy\nb. Cognitive restructuring", "b"),
        Question("Which of the following may reduce reinforcement of somatic behaviors?\na. Encouraging attention to symptoms\nb. Shifting attention toward healthier behaviors", "b"),
        Question("Which is an example of secondary gain in somatic disorders?\na. Relief from work responsibilities\nb. Resolution of unconscious conflict", "a"),
        Question("What is the focus of exposure therapy in somatic disorders?\na. Avoiding unpleasant emotions\nb. Confronting traumatic memories related to physical symptoms", "b"),
        Question("In illness anxiety disorder, the focus is on:\na. Multiple real symptoms\nb. Preoccupation with serious illness despite minimal symptoms", "b"),
        Question("Which disorder is NOT typically associated with a need to deceive others?\na. Malingering\nb. Somatic symptom disorder", "b"),
        Question("Which disorder involves the intentional faking of symptoms for external gain (e.g., money, avoiding work)?\na. Factitious disorder\nb. Malingering", "b"),
        Question("Is malingering classified as a mental disorder in the DSM-5?\na. Yes\nb. No", "b"),
        Question("Which model emphasizes the role of cultural norms in how symptoms are expressed?\na. Multicultural model\nb. Psychodynamic model", "a"),
        Question("Which of the following is a useful intervention for somatic symptom disorder?\na. Education and reassurance\nb. Invasive testing and unnecessary procedures", "a"),
        Question("Which therapy combines reinforcement, education, and restructuring negative beliefs about health?\na. Behavioral medicine therapy\nb. CBT (Cognitive Behavioral Therapy)", "b"),
        Question("What personality trait is associated with increased risk of somatic symptoms?\na. High emotional awareness\nb. Anxiety-prone or catastrophizing tendencies", "b"),
        Question("In psychophysiological disorders, stress:\na. Has no effect on illness progression\nb. Can trigger, worsen, or prolong physical illness", "b"),
]
psy12 = [
        Question("What type of training helps patients gain control over involuntary bodily processes?\na. Biofeedback training\nb. Classical conditioning", "a"),
        Question("What does the Social Readjustment Rating Scale measure?\na. Genetic predisposition to illness\nb. Stressful life events and their health impact", "b"),
        Question("What is the key feature of anorexia nervosa?\na. Purposefully taking in too many nutrients\nb. Purposefully restricting food intake leading to low body weight", "b"),
        Question("Which subtype of anorexia involves cutting out nearly all food and rigid dieting?\na. Restricting-type\nb. Binge-eating/purging-type", "a"),
        Question("Which subtype of anorexia involves self-induced vomiting and laxative use?\na. Restricting-type\nb. Binge-eating/purging-type", "b"),
        Question("What is a key psychological motivation in anorexia nervosa?\na. Craving high-calorie foods\nb. Intense fear of gaining weight", "b"),
        Question("What age group typically shows onset of anorexia nervosa?\na. 14–20 years\nb. 25–35 years", "a"),
        Question("How do individuals with anorexia perceive their body?\na. Accurate perception of body size\nb. Distorted perception, often seeing themselves as overweight", "b"),
        Question("Which of the following is a common medical complication of anorexia?\na. Increased bone density\nb. Amenorrhea (loss of menstruation)", "b"),
        Question("Which disorder includes repeated episodes of binge eating followed by compensatory behaviors?\na. Bulimia nervosa\nb. Binge-eating disorder", "a"),
        Question("How often must bulimic behaviors occur for diagnosis?\na. Daily for 6 weeks\nb. Weekly for 3 months", "b"),
        Question("What is the difference in body weight between anorexia and bulimia?\na. Bulimia usually involves very low weight\nb. Bulimia often involves normal or slightly overweight individuals", "b"),
        Question("Which eating disorder has the highest risk of electrolyte imbalance from purging?\na. Binge-eating disorder\nb. Bulimia nervosa", "b"),
        Question("What emotion often precedes a binge episode?\na. Joy\nb. Tension or anxiety", "b"),
        Question("Which of the following usually follows a binge?\na. Relief and satisfaction\nb. Shame, guilt, and self-blame", "b"),
        Question("Which eating disorder lacks compensatory behaviors like purging?\na. Bulimia nervosa\nb. Binge-eating disorder", "b"),
        Question("Which disorder is more likely to lead to obesity?\na. Anorexia nervosa\nb. Binge-eating disorder", "b"),
        Question("Which population has the highest rate of body dissatisfaction?\na. Women and girls\nb. Older adults", "a"),
]
psy13 = [
        Question("What is the most powerful contributor to eating disorders?\na. IQ level\nb. Body dissatisfaction", "b"),
        Question("Which psychological model emphasizes ego deficiencies and early mother-child interactions?\na. Psychodynamic model\nb. Behavioral model", "a"),
        Question("In the psychodynamic view, eating disorders stem from:\na. Positive parent-child relationships\nb. Ineffective parenting and identity confusion", "b"),
        Question("Which theory focuses on distorted thoughts about control and body image?\na. Cognitive-behavioral model\nb. Humanistic model", "a"),
        Question("Which of the following best describes the cognitive-behavioral model?\na. Food intake is driven by metabolic need\nb. Negative self-evaluation based on weight and shape", "b"),
        Question("Which disorder is commonly comorbid with eating disorders?\na. Substance use disorder\nb. Major depressive disorder", "b"),
        Question("What role do antidepressants play in eating disorder treatment?\na. Ineffective in most cases\nb. Helpful especially in bulimia and binge-eating disorder", "b"),
        Question("Which biological factor contributes to eating disorders?\na. High insulin production\nb. Genetic predisposition and brain circuit abnormalities", "b"),
        Question("Which brain structures are involved in regulating hunger and satiety?\na. Prefrontal cortex and thalamus\nb. Lateral and ventromedial hypothalamus", "b"),
        Question("What is the 'weight set point' theory?\na. Fixed calorie requirement per day\nb. The body resists weight change by adjusting metabolism and hunger", "b"),
        Question("Which societal group shows higher eating disorder risk?\na. Low-activity desk workers\nb. Models, dancers, and athletes", "b"),
        Question("Which cultural factor influences eating disorders?\na. Access to fresh produce\nb. Western ideals of thinness and media exposure", "b"),
        Question("Which family pattern may contribute to eating disorders?\na. Authoritative parenting\nb. Enmeshed family structures (overinvolved, overconcerned)", "b"),
        Question("Which cultural group has historically shown less body dissatisfaction?\na. White American women\nb. African American women", "b"),
        Question("Which personality trait is frequently associated with anorexia nervosa?\na. Impulsiveness\nb. Perfectionism", "b"),
]
psy14 = [
        Question("Which eating disorder shows more concern about pleasing others?\na. Bulimia nervosa\nb. Anorexia nervosa", "a"),
        Question("Which disorder is more likely to involve mood swings and impulsive behaviors?\na. Anorexia nervosa\nb. Bulimia nervosa", "b"),
        Question("Which medical issue is more common in bulimia nervosa than anorexia?\na. Low body temperature\nb. Dental erosion", "b"),
        Question("Which disorder shows higher rates of amenorrhea?\na. Anorexia nervosa\nb. Bulimia nervosa", "a"),
        Question("Which eating disorder is most likely to go unnoticed due to normal body weight?\na. Bulimia nervosa\nb. Anorexia nervosa", "a"),
        Question("Binge-eating disorder is defined by binge episodes with:\na. Compensatory behaviors\nb. No compensatory behaviors", "b"),
        Question("What is a common feeling experienced during binge-eating episodes?\na. Sense of control\nb. Loss of control", "b"),
        Question("Which eating disorder often includes secretive eating and intense shame?\na. Binge-eating disorder\nb. Anorexia nervosa", "a"),
        Question("How long must binge-eating episodes persist for diagnosis?\na. Weekly for 3 months\nb. Daily for 1 month", "a"),
        Question("Which of the following is NOT a diagnostic criterion for binge-eating disorder?\na. Vomiting after binges\nb. Eating unusually fast and when not hungry", "a"),
        Question("What is a typical onset age of binge-eating disorder?\na. Childhood\nb. Adulthood or later adolescence", "b"),
        Question("Which theory emphasizes control issues as central to eating disorders?\na. Humanistic theory\nb. Cognitive-behavioral theory", "b"),
        Question("Which theory argues that children with eating disorders misinterpret internal cues like hunger?\na. Psychodynamic theory\nb. Cognitive theory", "b"),
        Question("What does the biological model suggest about genetics and eating disorders?\na. No link exists\nb. Family history increases risk", "b"),
        Question("Which brain area shows abnormal activity in eating disorders?\na. Occipital lobe\nb. Insula and hypothalamus", "b"),
]
psy15 = [
        Question("Which peptide hormone is linked to satiety and may play a role in eating disorders?\na. GLP-1\nb. Oxytocin", "a"),
        Question("What does the weight set point theory explain?\na. Conscious weight goals\nb. The body’s natural tendency to maintain a certain weight range", "b"),
        Question("What societal influence contributes most to eating disorder development?\na. Academic competition\nb. Cultural emphasis on thinness", "b"),
        Question("What role does social media play in eating disorder risk?\na. It has no influence\nb. It can increase body dissatisfaction", "b"),
        Question("Which family dynamic is most associated with eating disorders?\na. Detached parenting\nb. Enmeshed family structure", "b"),
        Question("Which type of therapy is often used to address distorted beliefs in eating disorders?\na. Behavioral therapy\nb. Cognitive Behavioral Therapy (CBT)", "b"),
        Question("What is motivational interviewing used for in anorexia?\na. Encourage weight gain and treatment compliance\nb. Increase exercise adherence", "a"),
        Question("What is a key treatment goal in anorexia?\na. Reduce energy intake\nb. Restore proper nutrition and weight", "b"),
        Question("What role do dietitians play in eating disorder treatment?\na. Provide emotional counseling\nb. Guide nutritional rehabilitation", "b"),
        Question("What does family therapy target in eating disorder treatment?\na. Financial stress\nb. Family roles and communication", "b"),
        Question("Which treatment approach is most common in bulimia and binge-eating disorder?\na. Exposure therapy\nb. CBT plus medication", "b"),
        Question("What type of medications are often helpful for bulimia and binge-eating disorder?\na. Antidepressants (SSRIs)\nb. Antipsychotics", "a"),
        Question("Which disorder often responds best to behavioral weight restoration programs?\na. Binge-eating disorder\nb. Anorexia nervosa", "b"),
        Question("What is a long-term goal in all eating disorder treatment plans?\na. Increase perfectionism\nb. Address underlying psychological factors", "b"),
  ]

print("Welcome to your exam")
name = input("Enter Your Name: ")
classroom = input("Enter your class: ")
print("Hello " + name + " you are about to take a course for " + classroom)
print(" ")


while True:
  choice = input("This exam is split up into 15 parts. Which part would you like to take? 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15? Press 0 to Exit" )
  print(" ")
  if choice == "1":
      run_exam(psy1)
  elif choice == "2":
      run_exam(psy2)
  elif choice == "3":
      run_exam(psy3)
  elif choice == "4":
      run_exam(psy4)
  elif choice == "5":
      run_exam(psy5)
  elif choice == "6":
      run_exam(psy6)
  elif choice == "7":
      run_exam(psy7)
  elif choice == "8":
      run_exam(psy8)
  elif choice == "9":
      run_exam(psy9)
  elif choice == "10":
      run_exam(psy10)
  elif choice == "11":
      run_exam(psy11)
  elif choice == "12":
      run_exam(psy12)
  elif choice == "13":
      run_exam(psy13)
  elif choice == "14":
      run_exam(psy14)
  elif choice == "15":
      run_exam(psy15)
  elif choice == "0":
    break
  else:
    print("Improper input, please try again")
    print(" ")
