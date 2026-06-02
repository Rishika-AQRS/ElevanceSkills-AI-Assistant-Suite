import os
import xml.etree.ElementTree as et

def load_xml(folder_path):
    if not os.path.exists(folder_path):
        print(f"DEBUG: Folder does not exist: {folder_path}")
        return []
    texts=[]

    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path=os.path.join(folder_path, filename)
            try:
                tree=et.parse(file_path)
                root=tree.getroot()

                pair_count=0
                for qa in root.findall('.//QAPair'):
                    question_elem=qa.find('Question')
                    answer_elem=qa.find('Answer')

                    question=question_elem.text if question_elem is not None and question_elem.text else ""
                    answer=answer_elem.text if answer_elem is not None and answer_elem.text else ""
                    if question or answer:
                        full_text=f"Question: {question}\n\nAnswer: {answer}"
                        texts.append(full_text)
                        pair_count+=1
                print(f"DEBUG: Found {pair_count} QA pairs in {filename}")
            except Exception as e:
                print(f"DEBUG: Error parsing {filename}: {e}")
    print(f"DEBUG: Total QA pairs loaded: {len(texts)}")
    return texts



